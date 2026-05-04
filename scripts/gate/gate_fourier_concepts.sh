#!/usr/bin/env bash
set -euo pipefail

# 一键门禁：傅里叶分析 concepts 全量
#
# 说明：
# - 使用 shell glob 展开 concepts/*.md；如果目录为空则直接失败（防止误用）。

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

shopt -s nullglob
FILES=( "$ROOT/Content/傅里叶分析/concepts/"*.md )

if [[ ${#FILES[@]} -eq 0 ]]; then
  echo "ERROR: no concept files found under Content/傅里叶分析/concepts/"
  exit 1
fi

python "$ROOT/scripts/gate/katex_gate.py" "${FILES[@]}"
python "$ROOT/scripts/gate/callout_gate.py" "${FILES[@]}"

echo "OK: gate_fourier_concepts passed"

