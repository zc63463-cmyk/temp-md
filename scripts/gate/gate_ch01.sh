#!/usr/bin/env bash
set -euo pipefail

# 一键门禁：第01章 notes + 本章 cards（对齐其它章节 gate 口径）

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

FILES=(
  "$ROOT/Content/傅里叶分析/notes/第01章 Fourier分析的起源/index.md"
  "$ROOT/Content/傅里叶分析/notes/第01章 Fourier分析的起源/第01章 Fourier分析的起源 — 章节汇总.md"
  "$ROOT/Content/傅里叶分析/notes/第01章 Fourier分析的起源/第01章 Fourier分析的起源 — ingest(MOC).md"
  "$ROOT/Content/傅里叶分析/notes/第01章 Fourier分析的起源/1.1 弦振动.md"
  "$ROOT/Content/傅里叶分析/notes/第01章 Fourier分析的起源/1.2 热传导方程.md"
  "$ROOT/Content/傅里叶分析/notes/第01章 Fourier分析的起源/1.3 练习.md"
  "$ROOT/Content/傅里叶分析/notes/第01章 Fourier分析的起源/1.4 问题.md"

  # 本章关联 cards（方法/定理）
  "$ROOT/Content/傅里叶分析/cards/methods/MTH-分离变量法（PDE）.md"
  "$ROOT/Content/傅里叶分析/cards/methods/MTH-正交投影求系数.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-固定端波动方程的模态分解（正弦级数）.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-圆盘Dirichlet问题的分离变量表示（Fourier边界展开）.md"
)

python "$ROOT/scripts/gate/katex_gate.py" "${FILES[@]}"
python "$ROOT/scripts/gate/callout_gate.py" "${FILES[@]}"

echo "OK: gate_ch01 passed"
