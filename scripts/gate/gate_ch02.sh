#!/usr/bin/env bash
set -euo pipefail

# 一键门禁：第02章 notes + 本章 cards（按现有 cards 文件名列举）

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

FILES=(
  "$ROOT/Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/index.md"
  "$ROOT/Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/第02章 Fourier级数的基本性质 — 章节汇总.md"
  "$ROOT/Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/第02章 Fourier级数的基本性质 — ingest(MOC).md"
  "$ROOT/Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/2.1 问题的例子和公式.md"
  "$ROOT/Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/2.2 Fourier级数的唯一性.md"
  "$ROOT/Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/2.3 卷积.md"
  "$ROOT/Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/2.4 好核.md"
  "$ROOT/Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/2.5 Cesaro和Abel求和.md"
  "$ROOT/Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/2.6 练习.md"
  "$ROOT/Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/2.7 问题.md"

  # 本章关联 cards（对象/公式/定理/方法）
  "$ROOT/Content/傅里叶分析/cards/methods/MTH-Abel平均.md"
  "$ROOT/Content/傅里叶分析/cards/objects/OBJ-好核（近似恒等）.md"
  "$ROOT/Content/傅里叶分析/cards/formulas/FML-卷积使 Fourier 系数相乘.md"
  "$ROOT/Content/傅里叶分析/cards/formulas/FML-部分和=卷积（Dirichlet核）.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-好核逼近定理.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-Fejér定理（Cesàro求和一致收敛）.md"
  "$ROOT/Content/傅里叶分析/cards/theorems/THM-Fourier系数唯一性（Poisson核_Abel平均）.md"
)

python "$ROOT/scripts/gate/katex_gate.py" "${FILES[@]}"
python "$ROOT/scripts/gate/callout_gate.py" "${FILES[@]}"

echo "OK: gate_ch02 passed"

