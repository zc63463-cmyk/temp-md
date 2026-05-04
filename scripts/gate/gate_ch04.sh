#!/usr/bin/env bash
set -euo pipefail

# 一键门禁：第04章 notes + 本章 cards（按 ingest(MOC) 的链接清单列举）

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

FILES=(
  "$ROOT/Content/傅里叶分析/notes/第04章 Fourier级数的一些应用/index.md"
  "$ROOT/Content/傅里叶分析/notes/第04章 Fourier级数的一些应用/第04章 Fourier级数的一些应用 — 章节汇总.md"
  "$ROOT/Content/傅里叶分析/notes/第04章 Fourier级数的一些应用/第04章 Fourier级数的一些应用 — ingest(MOC).md"
  "$ROOT/Content/傅里叶分析/notes/第04章 Fourier级数的一些应用/4.1 等周不等式.md"
  "$ROOT/Content/傅里叶分析/notes/第04章 Fourier级数的一些应用/4.2 Weyl等分布定理.md"
  "$ROOT/Content/傅里叶分析/notes/第04章 Fourier级数的一些应用/4.3 处处不可微的连续函数.md"
  "$ROOT/Content/傅里叶分析/notes/第04章 Fourier级数的一些应用/4.4 圆上的热方程.md"

  # 本章关联 cards（定理/公式/方法）
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-等周不等式（Fourier证明）.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-Weyl判别准则（等分布⇔指数和）.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-无理旋转等分布（nα）.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-Weierstrass处处不可微（疏频）.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-热方程的Fourier表示解（圆周）.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-热核是好核（t↓0回收初值）.md"
  "$ROOT/Content/傅里叶分析/cards/formulas/FML-热核H_t（定义与关键性质）.md"
  "$ROOT/Content/傅里叶分析/cards/methods/MTH-尺度选择法（lacunary主频支配）.md"
)

python "$ROOT/scripts/gate/katex_gate.py" "${FILES[@]}"
python "$ROOT/scripts/gate/callout_gate.py" "${FILES[@]}"

echo "OK: gate_ch04 passed"

