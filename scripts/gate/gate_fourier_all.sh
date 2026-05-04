#!/usr/bin/env bash
set -euo pipefail

# 一键总验收：傅里叶分析（gate + scan）
#
# 目标：
# - 把日常“门禁 + 扫描”收敛为一条命令，避免漏跑
# - 本地与 CI 复用同一入口

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

# 1) 入口页（全局导航）门禁
bash "$ROOT/scripts/gate/gate_fourier_global.sh"

# 2) 全量门禁：concepts / cards
bash "$ROOT/scripts/gate/gate_fourier_concepts.sh"
bash "$ROOT/scripts/gate/gate_fourier_cards.sh"

# 3) 章节门禁（按现有章节范围）
for ch in 01 02 03 04 05 06 07 08 09; do
  bash "$ROOT/scripts/gate/gate_ch${ch}.sh"
done

# 4) 扫描（结构 + 链接 + duplicates + cards 真源）
python "$ROOT/scripts/scan/scan_notes.py" \
  --notes-root "$ROOT/Content/傅里叶分析/notes" \
  --concepts-root "$ROOT/Content/傅里叶分析/concepts" \
  --check-chapter-files \
  --check-overview \
  --check-links --classify-links \
  --check-navigation \
  --check-duplicates \
  --check-card-sources

echo "OK: gate_fourier_all passed"
