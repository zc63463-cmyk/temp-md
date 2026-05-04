#!/usr/bin/env bash
set -euo pipefail

# 一键门禁：第09章 notes + 本章 cards

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

FILES=(
  "$ROOT/Content/傅里叶分析/notes/第09章 积分/index.md"
  "$ROOT/Content/傅里叶分析/notes/第09章 积分/第09章 积分 — 章节汇总.md"
  "$ROOT/Content/傅里叶分析/notes/第09章 积分/第09章 积分 — ingest(MOC).md"
  "$ROOT/Content/傅里叶分析/notes/第09章 积分/9.1 Riemann可积函数的定义.md"
  "$ROOT/Content/傅里叶分析/notes/第09章 积分/9.2 多重积分.md"
  "$ROOT/Content/傅里叶分析/notes/第09章 积分/9.3 反常积分 R_d上的积分.md"

  "$ROOT/Content/傅里叶分析/cards/objects/OBJ-Riemann可积（上和_下和）.md"
  "$ROOT/Content/傅里叶分析/cards/objects/OBJ-振荡与零测集判别（Riemann可积）.md"
  "$ROOT/Content/傅里叶分析/cards/objects/OBJ-缓降函数（R_d反常积分接口）.md"
  "$ROOT/Content/傅里叶分析/cards/formulas/FML-U-L差=局部振荡加权和.md"
  "$ROOT/Content/傅里叶分析/cards/formulas/FML-球坐标积分公式（R_d）.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-Lebesgue判别（Riemann可积⇔不连续点零测）.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-连续函数的累次积分（矩体上Fubini）.md"
  "$ROOT/Content/傅里叶分析/cards/methods/MTH-ε细分法（压U-L到任意小）.md"
  "$ROOT/Content/傅里叶分析/cards/methods/MTH-截断+尾部控制实现无界域换序.md"
)

python "$ROOT/scripts/gate/katex_gate.py" "${FILES[@]}"
python "$ROOT/scripts/gate/callout_gate.py" "${FILES[@]}"

echo "OK: gate_ch09 passed"

