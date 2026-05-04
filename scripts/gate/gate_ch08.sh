#!/usr/bin/env bash
set -euo pipefail

# 一键门禁：第08章 notes + 本章 cards

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

FILES=(
  "$ROOT/Content/傅里叶分析/notes/第08章 Dirichlet定理/index.md"
  "$ROOT/Content/傅里叶分析/notes/第08章 Dirichlet定理/第08章 Dirichlet定理 — 章节汇总.md"
  "$ROOT/Content/傅里叶分析/notes/第08章 Dirichlet定理/第08章 Dirichlet定理 — ingest(MOC).md"
  "$ROOT/Content/傅里叶分析/notes/第08章 Dirichlet定理/8.1 一些基本的数论知识.md"
  "$ROOT/Content/傅里叶分析/notes/第08章 Dirichlet定理/8.2 Dirichlet定理.md"
  "$ROOT/Content/傅里叶分析/notes/第08章 Dirichlet定理/8.3 Dirichlet定理的证明.md"
  "$ROOT/Content/傅里叶分析/notes/第08章 Dirichlet定理/8.4 练习.md"
  "$ROOT/Content/傅里叶分析/notes/第08章 Dirichlet定理/8.5 问题.md"

  "$ROOT/Content/傅里叶分析/cards/objects/OBJ-Dirichlet特征（mod q）.md"
  "$ROOT/Content/傅里叶分析/cards/objects/OBJ-Dirichlet L函数（定义_Euler乘积）.md"
  "$ROOT/Content/傅里叶分析/cards/formulas/FML-Dirichlet特征正交关系（mod q）.md"
  "$ROOT/Content/傅里叶分析/cards/formulas/FML-同余类指示函数的character展开.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-Dirichlet定理（算术级数素数无穷多）.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-非主特征L(1,χ)非零.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-主特征与s=1极点的角色.md"
  "$ROOT/Content/傅里叶分析/cards/methods/MTH-Euler乘积对数化与发散比较（Dirichlet证明主线）.md"
)

python "$ROOT/scripts/gate/katex_gate.py" "${FILES[@]}"
python "$ROOT/scripts/gate/callout_gate.py" "${FILES[@]}"

echo "OK: gate_ch08 passed"
