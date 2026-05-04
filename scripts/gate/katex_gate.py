#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KaTeX 门禁（最小可复现版）

目标（对齐本库口径）：
1) 仅允许行内 $...$ 与“单行” $$ ... $$（同一行开闭）
2) 禁止：
   - 独占行 $$ 或 > $$（多行 display math 的分隔符）
   - 公式换行命令 \\\\
   - \\begin{...} / \\end{...}

用法：
  python katex_gate.py file1.md file2.md ...
退出码：
  0 通过；1 失败（会打印 file:line:reason）
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


STANDALONE_DD = re.compile(r"^\s*\$\$\s*$")
STANDALONE_QUOTED_DD = re.compile(r"^\s*>\s*\$\$\s*$")
DD_COUNT = re.compile(r"\$\$")


def iter_lines(path: Path):
    text = path.read_text(encoding="utf-8")
    return text.splitlines()


def strip_code_fences(lines: list[str]) -> list[tuple[int, str]]:
    """
    返回 (lineno, line) 列表，忽略 ``` fenced code block 内部内容。
    """
    out: list[tuple[int, str]] = []
    in_fence = False
    for i, line in enumerate(lines, start=1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            out.append((i, line))
            continue
        if not in_fence:
            out.append((i, line))
    return out


def remove_double_dollar_segments(line: str) -> str:
    """
    用空白替换同一行内的 $$...$$ 段，避免其内部的 $ 干扰单 $ 配对检查。
    若同一行出现多个段也可处理。
    """
    # 非贪婪，允许空内容 $$ $$（仍然会在其他规则里被抓）
    return re.sub(r"\$\$.*?\$\$", "", line)


def check_file(path: Path) -> list[str]:
    errs: list[str] = []
    lines = iter_lines(path)
    for lineno, line in strip_code_fences(lines):
        # 禁用模式扫描
        if "\\\\" in line:
            errs.append(f"{path}:{lineno}: 禁止出现 \\\\（LaTeX 换行）")
        if "\\begin{" in line or "\\end{" in line:
            errs.append(f"{path}:{lineno}: 禁止出现 \\\\begin{{}} / \\\\end{{}}")
        if STANDALONE_DD.match(line):
            errs.append(f"{path}:{lineno}: 禁止使用独占行 $$（仅允许单行 $$...$$）")
        if STANDALONE_QUOTED_DD.match(line):
            errs.append(f"{path}:{lineno}: 禁止使用 > $$（仅允许单行 $$...$$）")

        # $$ 必须同一行开闭：每行出现次数只能是 0 或 2 或 4 ...
        dd_n = len(DD_COUNT.findall(line))
        if dd_n % 2 == 1:
            errs.append(f"{path}:{lineno}: $$ 未在同一行闭合（只允许单行 $$...$$）")

        # 单 $ 的基本配对检查（忽略 $$...$$ 段与转义 \$）
        s = line.replace(r"\$", "")
        s = remove_double_dollar_segments(s)
        if s.count("$") % 2 == 1:
            errs.append(f"{path}:{lineno}: $ 未成对（可能存在未闭合行内公式）")

    return errs


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: python katex_gate.py <file1.md> <file2.md> ...", file=sys.stderr)
        return 2

    all_errs: list[str] = []
    for raw in argv[1:]:
        p = Path(raw)
        if not p.exists():
            all_errs.append(f"{p}: 文件不存在")
            continue
        if p.is_dir():
            all_errs.append(f"{p}: 需要传入文件路径，不接受目录")
            continue
        all_errs.extend(check_file(p))

    if all_errs:
        for e in all_errs:
            print(e)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

