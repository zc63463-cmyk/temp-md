#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Callout 连续性门禁（最小可复现版）

本库要求：callout 内部若需要空行，必须写成单独一行 `>`，不能出现真正的空行，
否则会导致 callout 在渲染/导出时意外断裂。

用法：
  python callout_gate.py file1.md file2.md ...
退出码：
  0 通过；1 失败（会打印 file:line:reason）
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


CALLOUT_START = re.compile(r"^\s*>\s*\[!\w+.*\]\s*")


def iter_lines(path: Path):
    text = path.read_text(encoding="utf-8")
    return text.splitlines()


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: python callout_gate.py <file1.md> <file2.md> ...", file=sys.stderr)
        return 2

    errs: list[str] = []
    for raw in argv[1:]:
        p = Path(raw)
        if not p.exists():
            errs.append(f"{p}: 文件不存在")
            continue
        if p.is_dir():
            errs.append(f"{p}: 需要传入文件路径，不接受目录")
            continue

        lines = iter_lines(p)
        in_fence = False
        in_callout = False

        for idx, line in enumerate(lines):
            lineno = idx + 1

            # fenced code block 内不检查（避免误报）
            if line.strip().startswith("```"):
                in_fence = not in_fence
                in_callout = False
                continue
            if in_fence:
                continue

            if CALLOUT_START.match(line):
                in_callout = True
                continue

            if in_callout:
                # callout 只在连续的 blockquote(以 > 开头)行内生效；
                # 空行会直接结束 blockquote。本库真正的“断裂风险”是：
                # 期望在 callout 内换段，却写成空行，导致下一行继续以 > 开头时断裂。
                if line == "":
                    prev = lines[idx - 1] if idx - 1 >= 0 else ""
                    nxt = lines[idx + 1] if idx + 1 < len(lines) else ""
                    if prev.lstrip().startswith(">") and nxt.lstrip().startswith(">") and not CALLOUT_START.match(nxt):
                        errs.append(f"{p}:{lineno}: callout 内换段空行缺少 '>'，请改为空行 '>'")
                    # 空行无论如何都结束 callout
                    in_callout = False
                    continue

                if not line.lstrip().startswith(">"):
                    in_callout = False

    if errs:
        for e in errs:
            print(e)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
