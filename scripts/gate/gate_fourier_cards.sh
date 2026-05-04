#!/usr/bin/env bash
set -euo pipefail

# 一键门禁：傅里叶分析 cards 全量
#
# 说明：
# - 递归展开 cards/**/*.md；如果目录为空则直接失败（防止误用）。

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

shopt -s globstar nullglob
FILES=( "$ROOT/Content/傅里叶分析/cards/"**/*.md )

if [[ ${#FILES[@]} -eq 0 ]]; then
  echo "ERROR: no card files found under Content/傅里叶分析/cards/"
  exit 1
fi

python "$ROOT/scripts/gate/katex_gate.py" "${FILES[@]}"
python "$ROOT/scripts/gate/callout_gate.py" "${FILES[@]}"

echo "OK: gate_fourier_cards passed"

