#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scan_notes.py

面向 Obsidian-Book-KB 的轻量“健康扫描”脚本（PR-0 用）：
- 章节三件套：index / 章节汇总 / ingest(MOC)
- ^overview 覆盖率
- wikilink / embed 断链（含 #^block-id）
- gate 覆盖：scripts/gate/gate_chXX.sh 是否存在

设计目标：
1) 快：只做文本级扫描（不解析 Obsidian 数据库）
2) 稳：对链接解析采用保守策略；宁可多报“可能问题”，也不漏掉硬断链
3) 可用于 PR 验收：发现问题返回 exit code=1
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional
import unicodedata


WIKILINK_RE = re.compile(r"(!)?\[\[([^\]]+)\]\]")
FRONTMATTER_RE = re.compile(r"\A---\s*$", re.M)


@dataclass
class Issue:
    kind: str
    path: Path
    message: str

    def format(self) -> str:
        return f"[{self.kind}] {self.path}: {self.message}"


@dataclass
class ResolveResult:
    status: str  # ok | missing | ambiguous
    path: Optional[Path] = None
    candidates: Optional[list[Path]] = None


def _normalize_name_key(name: str) -> str:
    """
    用于“弱归一化同名”检测（例如 Fejér核 vs Fejer核）：
    - NFKD 分解并移除组合音符
    - casefold
    - 去掉空白
    """
    s = unicodedata.normalize("NFKD", name)
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
    s = s.casefold()
    s = re.sub(r"\s+", "", s)
    return s


def _build_report(issues: list[Issue]) -> dict:
    by_kind: dict[str, int] = {}
    by_file: dict[str, int] = {}
    for it in issues:
        by_kind[it.kind] = by_kind.get(it.kind, 0) + 1
        k = str(it.path)
        by_file[k] = by_file.get(k, 0) + 1
    top_files = sorted(by_file.items(), key=lambda kv: (-kv[1], kv[0]))[:20]
    return {
        "total": len(issues),
        "by_kind": dict(sorted(by_kind.items(), key=lambda kv: (-kv[1], kv[0]))),
        "top_files": [{"path": p, "count": c} for p, c in top_files],
    }


def _format_report_md(report: dict) -> str:
    lines: list[str] = []
    lines.append(f"# Scan report")
    lines.append("")
    lines.append(f"- Total issues: **{report.get('total', 0)}**")
    lines.append("")
    lines.append("## By kind")
    lines.append("")
    lines.append("| kind | count |")
    lines.append("|---|---:|")
    for k, v in report.get("by_kind", {}).items():
        lines.append(f"| {k} | {v} |")
    lines.append("")
    lines.append("## Top files")
    lines.append("")
    lines.append("| file | count |")
    lines.append("|---|---:|")
    for it in report.get("top_files", []):
        lines.append(f"| {it['path']} | {it['count']} |")
    lines.append("")
    return "\n".join(lines)


def _iter_md_files(root: Path) -> Iterable[Path]:
    for p in root.rglob("*.md"):
        # 忽略 Obsidian 的隐藏目录
        if any(part.startswith(".") for part in p.parts):
            continue
        yield p


def _read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def _read_frontmatter(text: str) -> dict[str, str]:
    """
    极简 frontmatter 解析：
    - 只识别最顶端的 --- ... --- 区块
    - 只解析形如 `key: value` 的单行键值（不解析嵌套）
    用途：识别 redirect/status 等“机器可识别标记”。
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    out: dict[str, str] = {}
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            break
        m = re.match(r"^\s*([A-Za-z0-9_\-]+)\s*:\s*(.*?)\s*$", lines[i])
        if m:
            out[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return out


def _has_overview_block(text: str) -> bool:
    # block-id 需要独立一行：^overview
    return re.search(r"(?m)^\^overview\s*$", text) is not None


def _collect_block_ids(text: str) -> set[str]:
    # block-id：独立一行以 ^ 开头
    return set(re.findall(r"(?m)^\^([A-Za-z0-9][A-Za-z0-9_-]*)\s*$", text))


def _collect_headings(text: str) -> set[str]:
    # 保守：收集 # ... 标题行文本（去首尾空格）
    hs: set[str] = set()
    for m in re.finditer(r"(?m)^(#{1,6})\s+(.+?)\s*$", text):
        hs.add(m.group(2).strip())
    return hs


def _normalize_link_target(target: str) -> tuple[str, Optional[str], Optional[str]]:
    """
    解析 Obsidian wikilink 目标：
    - Note
    - Note#Heading
    - Note#^block
    允许 Note 中包含 |display（忽略显示名）
    返回：note_name, heading, block_id
    """
    # 表格中常写成 [[Note\|Alias]] 以避免与 Markdown table 的 | 冲突；
    # 这里做一次反转义，统一成 Note|Alias 再解析。
    target = target.replace(r"\|", "|")

    # 去掉显示文本：Note|Alias
    if "|" in target:
        target = target.split("|", 1)[0]
    note = target
    heading = None
    block = None
    if "#" in target:
        note, frag = target.split("#", 1)
        if frag.startswith("^"):
            block = frag[1:]
        else:
            heading = frag
    return note.strip(), heading, block


def _infer_vault_root(notes_root: Path) -> Optional[Path]:
    """
    从 notes_root 反推 vault 根目录（包含 Content/ 与 scripts/）。
    例如：.../Obsidian-Book-KB/Content/傅里叶分析/notes -> .../Obsidian-Book-KB
    """
    for p in [notes_root] + list(notes_root.parents):
        if (p / "Content").exists() and (p / "scripts").exists():
            return p
    return None


def _resolve_note_to_path(
    *,
    notes_root: Path,
    concepts_root: Optional[Path],
    cards_root: Optional[Path],
    vault_root: Path,
    current_file: Path,
    note_name: str,
) -> ResolveResult:
    """
    将 wikilink 的 note 名解析到文件路径。
    规则（保守）：
    - 若 note_name 含 "/"：视为 vault_root 下的相对路径（允许 .md/.pdf 等任意后缀；允许省略 .md）
    - 若 note_name 不含 "/"：
      1) 优先按“当前目录相对路径”解析（解决 [[index]] 这类章内链接）
      2) 其次在 notes_root 下查找唯一的 “{note_name}.md”
      3) 再在 cards 目录与 Content 下做兜底查找（解决 [[OBJ-...]] 这类 cards 链接）
    """
    if not note_name:
        return ResolveResult("missing")

    def try_with_md_suffix(p: Path) -> Optional[Path]:
        if p.exists():
            return p
        # 允许省略 .md；注意文件名本身可能含 "."（例如 "3.1 xxx.md"），
        # 因此不能依赖 Path.suffix == "" 判断。
        ps = str(p)
        if not ps.lower().endswith(".md"):
            q = Path(ps + ".md")
            if q.exists():
                return q
        return None

    # 1) 显式相对路径：相对于 vault_root
    if "/" in note_name:
        p = try_with_md_suffix(vault_root / note_name)
        return ResolveResult("ok", p) if p is not None else ResolveResult("missing")

    # 2) 当前目录相对（优先解决 [[index]] / [[something]] 的章内引用）
    cand = try_with_md_suffix(current_file.parent / note_name)
    if cand is not None:
        return ResolveResult("ok", cand)

    any_matches: list[Path] = []

    # 3) notes_root 下唯一匹配
    matches = list(notes_root.rglob(f"{note_name}.md"))
    if len(matches) == 1:
        return ResolveResult("ok", matches[0])
    any_matches += matches

    # 4) concepts_root 下唯一匹配（若启用）
    if concepts_root is not None and concepts_root.exists():
        m_concepts = list(concepts_root.rglob(f"{note_name}.md"))
        if len(m_concepts) == 1:
            return ResolveResult("ok", m_concepts[0])
        any_matches += m_concepts

    # 5) cards_root 兜底（解决 [[OBJ-...]] 等非 notes 文件）
    if cards_root is not None and cards_root.exists():
        m_cards = list(cards_root.rglob(f"{note_name}.md"))
        if len(m_cards) == 1:
            return ResolveResult("ok", m_cards[0])
        any_matches += m_cards

    # 6) Content 全局兜底
    content_root = vault_root / "Content"
    if content_root.exists():
        m3 = list(content_root.rglob(f"{note_name}.md"))
        if len(m3) == 1:
            return ResolveResult("ok", m3[0])
        any_matches += m3

    # 多匹配或未匹配：由调用方记录“歧义/不存在”
    uniq = sorted({p.resolve() for p in any_matches})
    if len(uniq) >= 2:
        return ResolveResult("ambiguous", candidates=uniq)
    return ResolveResult("missing")


def scan_chapter_files(notes_root: Path) -> list[Issue]:
    """
    扫描每个“第XX章 …”目录是否具备：
    - index.md
    - *— 章节汇总.md
    - *— ingest(MOC).md
    """
    issues: list[Issue] = []
    chapter_dirs = [p for p in notes_root.iterdir() if p.is_dir() and p.name.startswith("第") and "章" in p.name]
    for d in sorted(chapter_dirs):
        idx = d / "index.md"
        if not idx.exists():
            issues.append(Issue("missing_index", idx, "缺少章目录页 index.md"))

        has_summary = any(p.name.endswith("— 章节汇总.md") for p in d.glob("*.md"))
        if not has_summary:
            issues.append(Issue("missing_summary", d, "缺少“— 章节汇总.md”"))

        has_ingest = any(p.name.endswith("— ingest(MOC).md") for p in d.glob("*.md"))
        if not has_ingest:
            issues.append(Issue("missing_ingest", d, "缺少“— ingest(MOC).md”"))
    return issues


def scan_overview(notes_root: Path) -> list[Issue]:
    issues: list[Issue] = []
    for p in _iter_md_files(notes_root):
        text = _read_text(p)
        if not _has_overview_block(text):
            # 只对“节笔记/章级三件套/题解页”严格要求；这里先全量提示
            issues.append(Issue("missing_overview", p, "缺少独立行 block-id：^overview"))
    return issues


def scan_links(
    notes_root: Path,
    *,
    concepts_root: Optional[Path] = None,
    classify: bool = False,
) -> list[Issue]:
    issues: list[Issue] = []
    vault_root = _infer_vault_root(notes_root)
    if vault_root is None:
        issues.append(Issue("config", notes_root, "无法从 notes_root 反推 vault_root（需包含 Content/ 与 scripts/）"))
        return issues

    # 推导学科根目录（notes_root 通常为 Content/<学科>/notes）
    subject_root = notes_root.parent
    cards_root = (subject_root / "cards") if (subject_root / "cards").exists() else None

    # 缓存：路径 -> (block_ids, headings)
    cache: dict[Path, tuple[set[str], set[str]]] = {}

    def load_target(path: Path) -> tuple[set[str], set[str]]:
        if path not in cache:
            t = _read_text(path)
            cache[path] = (_collect_block_ids(t), _collect_headings(t))
        return cache[path]

    scan_roots: list[Path] = [notes_root]
    if concepts_root is not None:
        scan_roots.append(concepts_root)

    for root in scan_roots:
        if not root.exists():
            continue
        for p in _iter_md_files(root):
            text = _read_text(p)
            for m in WIKILINK_RE.finditer(text):
                target_raw = m.group(2).strip()
                note, heading, block = _normalize_link_target(target_raw)
                resolved = _resolve_note_to_path(
                    notes_root=notes_root,
                    concepts_root=concepts_root,
                    cards_root=cards_root,
                    vault_root=vault_root,
                    current_file=p,
                    note_name=note,
                )
                if resolved.status != "ok" or resolved.path is None:
                    if resolved.status == "ambiguous":
                        cand = resolved.candidates or []
                        shown = ", ".join(x.name for x in cand[:3])
                        suffix = f"（候选: {shown}{' …' if len(cand) > 3 else ''}）"
                        kind = "ambiguous_target" if classify else "broken_link"
                        issues.append(Issue(kind, p, f"目标歧义：[[{target_raw}]]{suffix}"))
                    else:
                        kind = "missing_target" if classify else "broken_link"
                        issues.append(Issue(kind, p, f"目标不存在：[[{target_raw}]]"))
                    continue
                target_path = resolved.path
                # 非 markdown（例如 pdf）只检查存在性
                if target_path.suffix.lower() != ".md":
                    continue
                if block is not None:
                    block_ids, _ = load_target(target_path)
                    if block not in block_ids:
                        kind = "unresolved_fragment" if classify else "missing_block"
                        issues.append(Issue(kind, p, f"目标缺少 block-id ^{block}：[[{target_raw}]] -> {target_path.name}"))
                if heading is not None:
                    _, headings = load_target(target_path)
                    if heading not in headings:
                        kind = "unresolved_fragment" if classify else "missing_heading"
                        issues.append(Issue(kind, p, f"目标缺少标题“{heading}”：[[{target_raw}]] -> {target_path.name}"))
    return issues


def scan_card_sources(
    notes_root: Path,
    *,
    concepts_root: Optional[Path] = None,
    max_inline_proof_lines: int = 25,
) -> list[Issue]:
    """
    cards 真源去重检查（PR-6）：
    - theorems/formulas/methods 类 cards 必须包含至少一个“真源入口”（链接或 embed），指向带 block-id 的 notes 位置
    - 若存在长 proof callout（超过阈值）且缺少真源入口，则报错
    - 若真源入口的 block-id 在目标文件中不存在，则报错
    """
    issues: list[Issue] = []
    vault_root = _infer_vault_root(notes_root)
    if vault_root is None:
        issues.append(Issue("config", notes_root, "无法从 notes_root 反推 vault_root（需包含 Content/ 与 scripts/）"))
        return issues

    subject_root = notes_root.parent
    cards_root = subject_root / "cards"
    if not cards_root.exists():
        issues.append(Issue("config", cards_root, "未找到 cards_root（期望 Content/<学科>/cards）"))
        return issues

    # 与 scan_links 同一套解析/缓存策略
    cache: dict[Path, tuple[set[str], set[str]]] = {}

    def load_target(path: Path) -> tuple[set[str], set[str]]:
        if path not in cache:
            t = _read_text(path)
            cache[path] = (_collect_block_ids(t), _collect_headings(t))
        return cache[path]

    def iter_card_files() -> Iterable[Path]:
        for p in _iter_md_files(cards_root):
            # 只检查 theorems/formulas/methods 三类（objects 允许没有 proof 真源）
            parts = set(p.parts)
            if "theorems" in parts or "formulas" in parts or "methods" in parts:
                yield p

    block_link_re = re.compile(r"(!)?\[\[([^\]]+#\^[^\]]+)\]\]")

    for p in iter_card_files():
        text = _read_text(p)
        has_source_link = False

        # 1) 真源入口：至少一个带 block-id 的 wikilink/embed，并且 block-id 在目标中存在
        for m in block_link_re.finditer(text):
            target_raw = m.group(2).strip()
            note, heading, block = _normalize_link_target(target_raw)
            if block is None:
                continue
            resolved = _resolve_note_to_path(
                notes_root=notes_root,
                concepts_root=concepts_root,
                cards_root=cards_root,
                vault_root=vault_root,
                current_file=p,
                note_name=note,
            )
            if resolved.status != "ok" or resolved.path is None:
                issues.append(Issue("card_missing_source", p, f"真源目标不存在或歧义：[[{target_raw}]]"))
                continue
            target_path = resolved.path
            if target_path.suffix.lower() != ".md":
                issues.append(Issue("card_missing_source", p, f"真源目标不是 md：[[{target_raw}]]"))
                continue
            block_ids, _ = load_target(target_path)
            if block not in block_ids:
                issues.append(Issue("card_source_fragment_missing", p, f"真源缺少 block-id ^{block}：[[{target_raw}]] -> {target_path.name}"))
                continue
            has_source_link = True

        if not has_source_link:
            issues.append(Issue("card_missing_source", p, "缺少真源入口（需要至少一个带 #^block-id 的 links/embed，建议指向 ^pf-*）"))

        # 2) 长 proof 阈值：存在长 proof callout 且缺少真源入口 → 报错
        # 只做轻量启发式：统计某个 proof/faq callout 连续引用行数
        lines = text.splitlines()
        i = 0
        while i < len(lines):
            line = lines[i]
            if re.match(r"^\s*>\s*\[!(proof|faq)\]", line, flags=re.I):
                j = i + 1
                count = 1
                while j < len(lines) and lines[j].lstrip().startswith(">"):
                    count += 1
                    j += 1
                if count > max_inline_proof_lines and not has_source_link:
                    issues.append(
                        Issue(
                            "card_inline_proof_too_long",
                            p,
                            f"疑似存在长 proof（{count} 行）且未转引真源（阈值 {max_inline_proof_lines}）",
                        )
                    )
                i = j
                continue
            i += 1

    return issues


def scan_duplicates(subject_root: Path) -> list[Issue]:
    """
    检测“弱归一化同名”：
    - 例如 Fejér核.md 与 Fejer核.md
    只做提示，不会自动修复。
    """
    issues: list[Issue] = []
    for sub in ["concepts", "cards"]:
        d = subject_root / sub
        if not d.exists():
            continue
        targets = [p for p in d.rglob("*.md") if not any(part.startswith(".") for part in p.parts)]
        groups: dict[str, list[Path]] = {}
        for p in targets:
            key = _normalize_name_key(p.stem)
            groups.setdefault(key, []).append(p)

        for key, ps in sorted(groups.items(), key=lambda kv: kv[0]):
            if len(ps) <= 1:
                continue
            redirects: list[Path] = []
            canonicals: list[Path] = []
            for p in ps:
                txt = _read_text(p)
                fm = _read_frontmatter(txt)
                is_redirect = fm.get("status") == "redirect"
                # 兼容旧页：若正文极短且包含“规范入口见/兼容历史链接”字样，也视为 redirect
                if not is_redirect:
                    short = len(txt.splitlines()) <= 40
                    if short and re.search(r"规范入口见|兼容历史链接", txt):
                        is_redirect = True
                (redirects if is_redirect else canonicals).append(p)

            if len(canonicals) == 1:
                # 合法：一个 canonical + 若干 redirect
                # 若 redirect 未声明 redirect_to，可提示但不致命（保持轻量）
                for r in redirects:
                    fm = _read_frontmatter(_read_text(r))
                    if fm.get("redirect_to") in (None, ""):
                        issues.append(Issue("redirect_missing_target", r, f"redirect 页缺少 redirect_to（key={key}）"))
                continue

            if len(canonicals) == 0:
                shown = ", ".join(sorted({x.name for x in ps})[:6])
                issues.append(Issue("redirect_without_canonical", d, f"存在 redirect 但缺少 canonical（key={key}）：{shown}"))
                continue

            shown = ", ".join(sorted({x.name for x in canonicals})[:6])
            issues.append(Issue("duplicate_name", d, f"存在多个 canonical（key={key}）：{shown}"))
    return issues


def scan_gates(gates_root: Path, chapters: Iterable[int]) -> list[Issue]:
    issues: list[Issue] = []
    for ch in chapters:
        fn = gates_root / f"gate_ch{ch:02d}.sh"
        if not fn.exists():
            issues.append(Issue("missing_gate", fn, "缺少章节 gate 脚本"))
    return issues


def scan_navigation(notes_root: Path) -> list[Issue]:
    """
    导航可验收检查（PR-9）：
    - notes/index.md 必须包含每个章节目录页链接
    - 学科首页 index.md 必须覆盖每个章节目录（至少包含章节目录名）
    - notes/全局索引.md 必须引用所有 notes/MOC-*.md
    """
    issues: list[Issue] = []
    subject_root = notes_root.parent

    subject_index = subject_root / "index.md"
    notes_index = notes_root / "index.md"
    global_index = notes_root / "全局索引.md"

    if not subject_index.exists():
        issues.append(Issue("nav_missing_file", subject_index, "缺少学科首页 index.md"))
        return issues
    if not notes_index.exists():
        issues.append(Issue("nav_missing_file", notes_index, "缺少 notes/index.md"))
        return issues
    if not global_index.exists():
        issues.append(Issue("nav_missing_file", global_index, "缺少 notes/全局索引.md"))
        return issues

    subject_text = _read_text(subject_index)
    notes_text = _read_text(notes_index)
    global_text = _read_text(global_index)

    chapter_dirs = [p for p in notes_root.iterdir() if p.is_dir() and p.name.startswith("第") and "章" in p.name]
    for d in sorted(chapter_dirs):
        # 章节目录页必须存在（scan_chapter_files 已查，这里只做导航覆盖）
        expect = f"Content/傅里叶分析/notes/{d.name}/index"
        if expect not in notes_text:
            issues.append(Issue("nav_missing_chapter_link", notes_index, f"缺少章节目录入口：{d.name}"))
        # 学科首页至少应出现章节目录名，避免“新增章但首页不更新”
        if d.name not in subject_text:
            issues.append(Issue("nav_missing_chapter_row", subject_index, f"学科首页缺少章节行：{d.name}"))

    moc_files = sorted([p for p in notes_root.glob("MOC-*.md") if p.is_file()])
    for p in moc_files:
        if p.name not in global_text and p.stem not in global_text:
            issues.append(Issue("nav_orphan_moc", p, "MOC 未在 notes/全局索引.md 注册入口"))

    return issues


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--notes-root", required=True, help="notes 根目录（例如 Content/傅里叶分析/notes）")
    ap.add_argument("--concepts-root", default=None, help="concepts 根目录（例如 Content/傅里叶分析/concepts，可选）")
    ap.add_argument("--gates-root", default=None, help="gate 根目录（例如 scripts/gate）")
    ap.add_argument("--chapters", default="1-9", help="章节范围，例如 1-9 或 1,2,5-9")

    ap.add_argument("--check-chapter-files", action="store_true")
    ap.add_argument("--check-overview", action="store_true")
    ap.add_argument("--check-links", action="store_true")
    ap.add_argument("--check-gates", action="store_true")
    ap.add_argument("--check-duplicates", action="store_true", help="检测弱归一化同名（重音/大小写/空格差异）")
    ap.add_argument("--check-card-sources", action="store_true", help="检查 cards 是否包含真源入口（PR-6）")
    ap.add_argument("--check-navigation", action="store_true", help="检查学科导航页与 MOC 注册（PR-9）")
    ap.add_argument("--max-inline-proof-lines", type=int, default=25, help="cards 内联 proof 允许的最大连续引用行数（超过需转引真源）")

    ap.add_argument(
        "--classify-links",
        action="store_true",
        help="将 broken_link 细分为 missing_target / ambiguous_target，并将缺失 fragment 统一为 unresolved_fragment（默认保持旧 kind 以向后兼容）",
    )
    ap.add_argument(
        "--format",
        default="text",
        choices=["text", "md", "json"],
        help="输出格式：text（默认，兼容旧输出）/ md / json",
    )
    ap.add_argument("--report", default=None, help="将聚合报表写入指定路径（md/json 由 --format 决定）")

    args = ap.parse_args(argv)

    notes_root = Path(args.notes_root).resolve()
    if not notes_root.exists():
        print(f"ERROR: notes_root not exists: {notes_root}", file=sys.stderr)
        return 2

    concepts_root = Path(args.concepts_root).resolve() if args.concepts_root else None
    if concepts_root is not None and not concepts_root.exists():
        print(f"ERROR: concepts_root not exists: {concepts_root}", file=sys.stderr)
        return 2

    def parse_chapters(spec: str) -> list[int]:
        out: set[int] = set()
        for part in spec.split(","):
            part = part.strip()
            if not part:
                continue
            if "-" in part:
                a, b = part.split("-", 1)
                out.update(range(int(a), int(b) + 1))
            else:
                out.add(int(part))
        return sorted(out)

    chapters = parse_chapters(args.chapters)

    issues: list[Issue] = []
    if args.check_chapter_files:
        issues += scan_chapter_files(notes_root)
    if args.check_overview:
        issues += scan_overview(notes_root)
    if args.check_links:
        issues += scan_links(notes_root, concepts_root=concepts_root, classify=args.classify_links)
    if args.check_gates:
        if not args.gates_root:
            print("ERROR: --gates-root is required when --check-gates is set", file=sys.stderr)
            return 2
        issues += scan_gates(Path(args.gates_root).resolve(), chapters)
    if args.check_duplicates:
        issues += scan_duplicates(notes_root.parent)
    if args.check_card_sources:
        issues += scan_card_sources(
            notes_root,
            concepts_root=concepts_root,
            max_inline_proof_lines=args.max_inline_proof_lines,
        )
    if args.check_navigation:
        issues += scan_navigation(notes_root)

    if issues:
        if args.format == "text" and not args.report:
            print("Scan issues:")
            for it in issues:
                print(" - " + it.format())
        else:
            report = _build_report(issues)
            payload = {
                "issues": [{"kind": it.kind, "path": str(it.path), "message": it.message} for it in issues],
                "report": report,
            }
            if args.format == "json":
                out = json.dumps(payload, ensure_ascii=False, indent=2)
            else:
                out = _format_report_md(report) + "\n" + "\n".join(
                    ["## Issues", ""] + [f"- `{it.kind}` {it.path}: {it.message}" for it in issues]
                )
            if args.report:
                Path(args.report).write_text(out, encoding="utf-8")
            print(out)
        return 1

    # 无 issue：默认保持旧输出；若用户要求 report/非 text 格式，则仍输出空报表
    if args.report or args.format != "text":
        report = _build_report([])
        payload = {"issues": [], "report": report}
        if args.format == "json":
            out = json.dumps(payload, ensure_ascii=False, indent=2)
        else:
            out = _format_report_md(report)
        if args.report:
            Path(args.report).write_text(out, encoding="utf-8")
        print(out)
        return 0

    print("OK: scan passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
