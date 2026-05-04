#!/usr/bin/env bash
set -euo pipefail

# 一键门禁：第07章 notes（含练习/问题）

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

FILES=(
  "$ROOT/Content/傅里叶分析/notes/第07章 有限Fourier分析/index.md"
  "$ROOT/Content/傅里叶分析/notes/第07章 有限Fourier分析/第07章 有限Fourier分析 — 章节汇总.md"
  "$ROOT/Content/傅里叶分析/notes/第07章 有限Fourier分析/第07章 有限Fourier分析 — ingest(MOC).md"
  "$ROOT/Content/傅里叶分析/notes/第07章 有限Fourier分析/7.1 Z_N上的Fourier分析.md"
  "$ROOT/Content/傅里叶分析/notes/第07章 有限Fourier分析/7.2 有限Abel群上的Fourier分析.md"
  "$ROOT/Content/傅里叶分析/notes/第07章 有限Fourier分析/7.3 练习.md"
  "$ROOT/Content/傅里叶分析/notes/第07章 有限Fourier分析/7.4 问题.md"
)

python "$ROOT/scripts/gate/katex_gate.py" "${FILES[@]}"
python "$ROOT/scripts/gate/callout_gate.py" "${FILES[@]}"

echo "OK: gate_ch07 passed"
