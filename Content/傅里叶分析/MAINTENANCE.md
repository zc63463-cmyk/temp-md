---
title: "傅里叶分析知识库维护手册"
type: maintenance
tags:
  - 傅里叶分析
  - 维护
  - 规范
date: 2026-04-25
cssclasses:
  - wide-page
---

> [!abstract] 目的
> 这份手册用于把“写作习惯”变成“可验收制度”，降低内容漂移与格式回退风险。  
> 核心原则：**notes 真源**、**cards 入口**、**concepts 节点**，并由 gate/scan 提供硬门槛。
^overview

## 1. 分工总则（必须遵守）
### 1.1 notes：真源（Proof/长推导只维护一份）
- 完整证明、长推导、长估计，只允许维护在 `notes/` 中（并配 block-id）。
- cards/concepts 不允许复制同一段长证明（避免双写漂移）。

### 1.2 cards：可调用入口（短、结构化、可复用）
cards 的目标是“快速调用”，而不是“再写一份讲义”：
- 结论（可调用口径）
- 条件作用（每条假设为什么需要）
- 最短证明骨架（3–7 行，非完备证明）
- 真源入口（链接或 embed 到 notes 的真源 block）

### 1.3 concepts：可复用知识节点
concepts 页用于“定义 + 关键性质 + 误区 + 回链”，不承担长证明。完成度标准见 `Content/傅里叶分析/concepts/index.md`。

## 2. 硬门槛（格式）
### 2.1 KaTeX 门禁（重要）
门禁由 `scripts/gate/katex_gate.py` 执行，必须满足：
- 仅允许行内 `$...$` 与单行 `$$...$$`（开闭必须在同一行）
- 禁止 LaTeX 换行符
- 禁止 begin/end 环境
- 禁止独占行 `$$`（包含 callout 中的 `> $$`）

### 2.2 callout 门禁（重要）
门禁由 `scripts/gate/callout_gate.py` 执行：
- callout 内不允许真实空行；需要换段时，用单独一行 `>` 占位

## 3. 真源 block-id 约定（notes）
建议统一使用以下前缀（便于卡片与扫描脚本识别）：
- 定义：`^def-...`
- 引理：`^lem-...`
- 定理：`^thm-...`
- 证明：`^pf-...`

> [!note] 最低要求
> 若 cards 需要引用“证明真源”，对应 notes 必须提供 `^pf-...`。

## 4. cards 模板（建议复制）
### 4.1 theorem/formula/method 通用模板
```markdown
---
title: "..."
type: card
card_type: theorems   # or formulas/methods/objects
tags:
  - 傅里叶分析
date: 2026-04-25
cssclasses:
  - wide-page
---

> [!abstract] 结论（一句话）
> ...
^overview

## 条件与口径
- ...

## 证明骨架（只写 3–7 行）
- ...

## 真源（勿在本卡重复维护）
见：[[Content/傅里叶分析/notes/第XX章 .../x.y ...#^pf-xxx]]
```

### 4.2 何时用 embed（而不是链接）
仅当你希望卡片“打开即读真源证明”时使用：
```markdown
![[Content/傅里叶分析/notes/第XX章 .../x.y ...#^pf-xxx]]
```

## 5. redirect 页规范（concepts/cards/notes 兼容旧名）
同一概念只允许一个 canonical 正文页；其余别名/重音符/旧名页必须是 redirect：
- frontmatter 建议：
  - `status: redirect`
  - `redirect_to: "Content/傅里叶分析/concepts/XXX"`（canonical 路径）
- 正文建议保持极短，只说明“该条目用于兼容历史链接”，并给出 canonical 链接。

## 6. 本地验收命令（推荐工作流）
### 6.1 最小验收集（写作/小改动后）
```bash
bash scripts/gate/gate_fourier_global.sh
python scripts/scan/scan_notes.py \
  --notes-root "Content/傅里叶分析/notes" \
  --concepts-root "Content/傅里叶分析/concepts" \
  --check-links --classify-links
```

### 6.2 结构性改动/批量移动后（全量）
```bash
bash scripts/gate/gate_fourier_all.sh
```

