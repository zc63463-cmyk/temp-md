#!/usr/bin/env bash
set -euo pipefail

# 一键门禁：第06章 notes + ingest(MOC)

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

FILES=(
  "$ROOT/Content/傅里叶分析/notes/第06章 R_d上的Fourier变换/index.md"
  "$ROOT/Content/傅里叶分析/notes/第06章 R_d上的Fourier变换/第06章 R_d上的Fourier变换 — 章节汇总.md"
  "$ROOT/Content/傅里叶分析/notes/第06章 R_d上的Fourier变换/第06章 R_d上的Fourier变换 — ingest(MOC).md"

  "$ROOT/Content/傅里叶分析/notes/第06章 R_d上的Fourier变换/6.1 预备知识.md"
  "$ROOT/Content/傅里叶分析/notes/第06章 R_d上的Fourier变换/6.2 Fourier变换的初等理论.md"
  "$ROOT/Content/傅里叶分析/notes/第06章 R_d上的Fourier变换/6.3 R_d_x_R上的波动方程.md"
  "$ROOT/Content/傅里叶分析/notes/第06章 R_d上的Fourier变换/6.4 径向对称与Bessel函数.md"
  "$ROOT/Content/傅里叶分析/notes/第06章 R_d上的Fourier变换/6.5 Radon变换及其应用.md"
  "$ROOT/Content/傅里叶分析/notes/第06章 R_d上的Fourier变换/6.6 练习.md"
  "$ROOT/Content/傅里叶分析/notes/第06章 R_d上的Fourier变换/6.7 问题.md"
)

python "$ROOT/scripts/gate/katex_gate.py" "${FILES[@]}"
python "$ROOT/scripts/gate/callout_gate.py" "${FILES[@]}"

echo "OK: gate_ch06 passed"
