#!/usr/bin/env bash
set -euo pipefail

# 一键门禁：第05章 notes + ingest(MOC) + 本章 cards（含 5.5/5.6）

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

FILES=(
  "$ROOT/Content/傅里叶分析/notes/第05章 R上的Fourier变换/index.md"
  "$ROOT/Content/傅里叶分析/notes/第05章 R上的Fourier变换/第05章 R上的Fourier变换 — 章节汇总.md"
  "$ROOT/Content/傅里叶分析/notes/第05章 R上的Fourier变换/5.1 Fourier变换的基本理论.md"
  "$ROOT/Content/傅里叶分析/notes/第05章 R上的Fourier变换/5.2 偏微分方程中的一些应用.md"
  "$ROOT/Content/傅里叶分析/notes/第05章 R上的Fourier变换/5.3 Poisson求和公式.md"
  "$ROOT/Content/傅里叶分析/notes/第05章 R上的Fourier变换/5.4 Heisenberg不确定性原理.md"
  "$ROOT/Content/傅里叶分析/notes/第05章 R上的Fourier变换/5.5 练习.md"
  "$ROOT/Content/傅里叶分析/notes/第05章 R上的Fourier变换/5.6 问题.md"
  "$ROOT/Content/傅里叶分析/notes/第05章 R上的Fourier变换/第05章 R上的Fourier变换 — ingest(MOC).md"

  "$ROOT/Content/傅里叶分析/cards/theorems/THM-Fourier反演公式（R上）.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-Plancherel定理（R上）.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-热方程的Fourier乘子解（R上）.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-Poisson求和公式.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-Heisenberg不确定性原理（Fourier形式）.md"
)

python "$ROOT/scripts/gate/katex_gate.py" "${FILES[@]}"
python "$ROOT/scripts/gate/callout_gate.py" "${FILES[@]}"

echo "OK: gate_ch05 passed"
