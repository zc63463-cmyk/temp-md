#!/usr/bin/env bash
set -euo pipefail

# 一键门禁：傅里叶分析全局导航页（首页 / notes索引 / 全局索引 / cards&concepts索引）
#
# 目的：让“入口页”也受 KaTeX/callout 门禁约束，避免静默引入格式违例。

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

FILES=(
  "$ROOT/Content/index.md"
  "$ROOT/Content/Wiki/index.md"

  "$ROOT/Content/傅里叶分析/index.md"
  "$ROOT/Content/傅里叶分析/notes/index.md"
  "$ROOT/Content/傅里叶分析/notes/全局索引.md"
  "$ROOT/Content/傅里叶分析/cards/index.md"
  "$ROOT/Content/傅里叶分析/concepts/index.md"
)

python "$ROOT/scripts/gate/katex_gate.py" "${FILES[@]}"
python "$ROOT/scripts/gate/callout_gate.py" "${FILES[@]}"

echo "OK: gate_fourier_global passed"

