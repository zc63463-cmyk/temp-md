#!/usr/bin/env bash
set -euo pipefail

# 一键门禁：第03章 notes + 本章 cards（按 ingest(MOC) 的链接清单列举）

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

FILES=(
  "$ROOT/Content/傅里叶分析/notes/第03章 Fourier级数的收敛性/index.md"
  "$ROOT/Content/傅里叶分析/notes/第03章 Fourier级数的收敛性/第03章 Fourier级数的收敛性 — 章节汇总.md"
  "$ROOT/Content/傅里叶分析/notes/第03章 Fourier级数的收敛性/第03章 Fourier级数的收敛性 — ingest(MOC).md"
  "$ROOT/Content/傅里叶分析/notes/第03章 Fourier级数的收敛性/3.1 Fourier级数的均方收敛.md"
  "$ROOT/Content/傅里叶分析/notes/第03章 Fourier级数的收敛性/3.2 逐点收敛.md"
  "$ROOT/Content/傅里叶分析/notes/第03章 Fourier级数的收敛性/3.3 练习.md"
  "$ROOT/Content/傅里叶分析/notes/第03章 Fourier级数的收敛性/3.4 问题.md"

  # 本章关联 cards（对象/公式/定理/方法/估计）
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-Bessel不等式（L2）.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-Parseval恒等式（圆周Plancherel）.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-Fourier部分和的L2均方收敛（S_N f→f）.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-Dirichlet点态收敛定理（BV_分段光滑）.md"

  "$ROOT/Content/傅里叶分析/cards/formulas/FML-L2内积（圆周归一化）.md"
  "$ROOT/Content/傅里叶分析/cards/formulas/FML-Fourier系数与部分和（定义）.md"
  "$ROOT/Content/傅里叶分析/cards/formulas/FML-Dirichlet核闭式（sin比）.md"
  "$ROOT/Content/傅里叶分析/cards/methods/MTH-对称化（偶核→左右平均）.md"
  "$ROOT/Content/傅里叶分析/cards/objects/OBJ-有界变差（BV）在Dirichlet收敛中的角色.md"

  "$ROOT/Content/傅里叶分析/cards/theorems/THM-ℓ2空间完备性（Hilbert）.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-Wirtinger–Poincaré不等式（周期_均值为0）.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-导数在L2则Fourier级数绝对收敛.md"
  "$ROOT/Content/傅里叶分析/cards/formulas/FML-共轭Dirichlet核闭式.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/EST-共轭Dirichlet核L1对数估计.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-Euler型恒等式（cot求和）.md"
  "$ROOT/Content/傅里叶分析/cards/formulas/FML-ζ(2m) 与 Bernoulli 数.md"
  "$ROOT/Content/傅里叶分析/cards/formulas/FML-Bernoulli多项式 Fourier 展开.md"
)

python "$ROOT/scripts/gate/katex_gate.py" "${FILES[@]}"
python "$ROOT/scripts/gate/callout_gate.py" "${FILES[@]}"

echo "OK: gate_ch03 passed"

