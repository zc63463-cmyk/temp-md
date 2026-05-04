# Obsidian 知识库：从「数学」迁移到「算法 / 数据结构 / CPP」的构建方案

## Summary（摘要）
你当前的知识库流程是「上传书籍/课程素材 → 学习做笔记 → 存入 Obsidian 并长期维护」。本方案在你提供的 SCHEMA 模板基础上，把学科域从“数学”迁移为「算法 / 数据结构 / CPP」，并以“按课程/书籍（track）组织”为核心，落地统一的：目录结构、Domain 注册、标签体系、笔记/Wiki 模板、Learn→Ingest→Maintenance 工作流、索引页与一致性校验。

本方案的执行结果是：你可以持续把新书/新课程按同一套规则纳入知识库，并且能稳定维护跨章节的概念页（Wiki）与导航索引，避免未来返工。

---

## Current State Analysis（现状分析）
### 输入与约束
1. 目标平台：Obsidian 本地库（用户已确认）。
2. 迁移重点：统一分类体系（用户已确认）。
3. 内容来源：你会持续上传书籍/课程材料，由你学习后产出笔记并入库（用户补充）。
4. 组织方式：按课程/书籍（用户已确认）。
5. 现有规范来源：你上传的模板文件《知识库构建配置参考模板》([View file](computer:///workspace/.uploads/ce68c01a-4278-439b-9a76-e2c64dce557f_SCHEMA-TEMPLATE%20(1).md))，其核心包含：
   - 四层内容模型（Navigation / Wiki / Raw Notes / Canvas）
   - 目录结构（Content/Wiki/SCHEMA.md、Wiki/index、log、health 等）
   - 命名规则、Tag Taxonomy、Domain 注册表
   - Learn Workflow（学完一章的产出与验证）、Ingest（提炼 Wiki）、Maintenance（健康检查）

### 迁移风险点（需要在设计里规避）
1. **“C++”命名不适合作为目录名**：跨平台同步、发布或 URL 常有编码/转义问题；应使用 `CPP` 作为目录名，用 `title/aliases` 呈现为 “C++”。
2. **跨域同名概念冲突**：算法/数据结构/CPP 可能出现同名术语（如“栈”“堆”），需要消歧策略（文件名消歧或别名链接）。
3. **链接可维护性**：Obsidian 内链应优先使用 `[[wikilinks]]`，并用 aliases 处理“显示名 ≠ 文件名”的情况。

---

## Assumptions & Decisions（假设与决策）
### 已做出的决策（本计划按此执行）
1. 知识库根结构沿用模板的 `Content/` 体系（Navigation + Wiki + 各学科域）。
2. 新增 3 个 Domain（学科域）：
   - `算法`（目录名：`算法`）
   - `数据结构`（目录名：`数据结构`）
   - `C++`（目录名：`CPP`，显示名通过 frontmatter 处理）
3. “按课程/书籍组织”采用 **track 模型**：每个 Domain 下都有 `tracks/`，notes/canvas 按 track 分流。
4. 不强依赖任何 Obsidian 插件（如 Dataview）：索引页采用手工维护 + Maintenance 校验的方式；若你已用插件，可在执行阶段再做增强，但不作为本方案前置条件。

### 执行阶段需要你提供/确认的信息（不影响规划，但影响填充占位符）
1. 每个 Domain 的首批 track 列表（书名/课程名 + 简短代号，如 `CLRS` / `CP3` / `侯捷C++`）。
2. 你希望“章节/讲次”的编号格式：
   - 书籍型：`第01章` + `{节号}`（推荐沿用模板）
   - 课程型：`Lecture-01` + `{小节}`（若你课程居多可改）

---

## Proposed Changes（改动方案：文件/目录级别，含 why/how）
> 说明：以下路径以你的 Obsidian vault 为基准描述；实际执行时在你 vault 中创建同名目录与文件即可。

### A. 建立全局骨架（Navigation + Wiki 元数据层）
#### A1. 创建/更新全局入口页
1. **创建** `Content/index.md`
   - **Why**：作为知识库“总入口”，提供 3 个 Domain 的入口与 track 列表。
   - **How**：用 Obsidian wikilinks 指向：
     - `[[算法/index]]`、`[[数据结构/index]]`、`[[CPP/index|C++]]`
     - 并在各 Domain 下列出 `tracks/` 入口页。

#### A2. 落地 SCHEMA 与全局索引/日志/健康报告
1. **创建** `Content/Wiki/SCHEMA.md`
   - **Why**：把你上传的模板固化成“本库唯一规范源”，后续新内容都按此执行。
   - **How**：
     - 将模板复制到该路径（模板建议的默认位置）。
     - 全量替换占位符 `{学科}` `{日期}` 等，并将“数学”域改为 3 个新域（见后续 B1）。
2. **创建** `Content/Wiki/index.md`
   - **Why**：作为跨学科 Wiki 页的总目录（concepts/theorems/comparisons/queries）。
   - **How**：
     - 按 Domain 分 section：算法/数据结构/CPP；
     - 每个 section 下维护四类表格（可先为空表结构）。
3. **创建** `Content/Wiki/log.md`（append-only）
   - **Why**：记录初始化、每次 ingest、每次 lint/修复，便于回溯。
   - **How**：每次执行“新增域/新增章节/maintenance”在末尾追加一条记录。
4. **创建** `Content/Wiki/health/` 目录与健康报告模板
   - **Why**：承接 Maintenance 输出（断链、计数不一致、命名违规等）。
   - **How**：按日期生成 `YYYY-MM-DD.md`，并在 `log.md` 追加维护记录。

---

### B. 建立 3 个 Domain（学科域）与“按课程/书籍”的 track 模型
#### B1. 创建每个 Domain 的目录与首页
对每个 Domain（算法/数据结构/CPP）：
1. **创建目录**：
   - `Content/{Domain}/tracks/`
   - `Content/{Domain}/concepts/`
   - `Content/{Domain}/theorems/`
   - `Content/{Domain}/comparisons/`
   - `Content/{Domain}/queries/`
   - `Content/{Domain}/notes/`
   - `Content/{Domain}/canvas/`
2. **创建** `Content/{Domain}/index.md`
   - **Why**：作为该学科的“导航中枢”（track 列表、进度、Wiki 统计入口）。
   - **How**：固定包含三块：
     1) Track 列表表格（书名/代号/进度/章节数/笔记数/Wiki 贡献数）
     2) 指向本域的 Wiki 分类入口（concepts/theorems/...）
     3) 学习路线入口（可先放占位链接）

#### B2. Track（课程/书籍）入口页规则
对每个 track（例如 `CLRS`）：
1. **创建** `Content/{Domain}/tracks/{track}.md`
   - **Why**：按书组织 notes/canvas，并提供章节入口与进度管理。
   - **How**：固定结构建议：
     - 教材/课程信息表（书名、作者、版次、链接/ISBN）
     - 章节/讲次列表（每行链接到章节汇总页）
     - 当前进度（统一符号体系，如 ⬜/🟨/✅）
     - “Wiki 贡献入口”：本书新增/更新的概念页索引

#### B3. Notes/Canvas 按 track 分流的最终路径规则
1. 节笔记：
   - `Content/{Domain}/notes/{track}/第01章 {章标题}/{节号} {节标题}.md`
2. 章节汇总：
   - `Content/{Domain}/notes/{track}/第01章 {章标题}/第01章 {章标题} — 章节汇总.md`
3. Canvas：
   - `Content/{Domain}/canvas/{track}/第01章 {章标题}/{节号} {节标题}.canvas`

---

### C. 统一 Tag Taxonomy（标签层级）与命名规范
#### C1. 标签体系（写入 SCHEMA.md 并强制执行）
沿用模板结构并做 CS 约束化：
1. Tag 统一为：`#学习/{domain}/{子领域}/{关键词}`
2. `domain` 仅允许：`算法` / `数据结构` / `CPP`
3. 推荐示例：
   - `#学习/算法/DP/背包`
   - `#学习/数据结构/树/线段树`
   - `#学习/CPP/STL/vector`

#### C2. 命名规范（补充到 SCHEMA.md）
1. **目录名**：`CPP` 代替 `C++`
2. **文件名禁忌**：禁止 `/`；用 `_` 替代（模板已有，继续沿用）
3. **C++ 符号页**：文件名使用安全形式（如 `std-vector.md`），在 `aliases` 中加入 `std::vector`；链接时用 `[[std-vector|std::vector]]`
4. **同名概念消歧**（二选一，写死一种）：
   - 方案 1（推荐）：文件名加括号消歧：`堆（数据结构）.md`、`堆（内存）.md`
   - 方案 2：文件名不消歧，但所有链接强制用 `[[文件名|显示名]]` + aliases（维护成本更高，不推荐）

---

### D. 统一笔记/ Wiki 页的 frontmatter（Properties）与 Obsidian 语法规范
> 本部分依据 Obsidian 规范：使用 YAML frontmatter（properties）、wikilinks、callouts。

#### D1. 节笔记（type=note）frontmatter 规范
在 SCHEMA.md 写入并作为模板化字段（字段名固定，减少后期脚本/检索成本）：
```yaml
---
title: "{节号} {节标题}"
type: note
domain: "{算法|数据结构|CPP}"
track: "{课程或书籍短名}"
book: "{书名或课程名}"
chapter: "第{N}章 {章标题}"
section: "{节号或Lecture-XX}"
author: "{作者/讲者}"
source:
  - "{URL/ISBN/课程主页}"
tags:
  - "学习/{domain}/{子领域}/{关键词}"
aliases:
  - "{英文名/别名}"
date: YYYY-MM-DD
cssclasses:
  - wide-page
---
```

#### D2. Wiki 概念页（type=concept）frontmatter 规范
```yaml
---
title: "{概念名}"
type: concept
domain: "{算法|数据结构|CPP}"
track:
  - "{可选：来源track1}"
tags:
  - "学习/{domain}/{子领域}/{关键词}"
sources:
  - "{来源}"
related:
  - "[[相关概念]]"
date: YYYY-MM-DD
---
```

#### D3. Callouts（强化 CS 笔记可复用性）
在 SCHEMA.md 中把 callout 语义写死：
- `[!abstract]`：本节一句话定位 + 要点清单（必须含 `==高亮==` 术语）
- `[!def]`：形式化定义（状态/不变式/复杂度/接口契约）
- `[!tip]`：套路/模板（DP 设计法、二分答案、单调栈模型等）
- `[!example]`：例题/代码（建议附 I/O 与关键注释）
- `[!warning]`：坑点（边界、溢出、UB、复杂度误判）
- `[!info]`：扩展（来源、变体、标准条款链接）
- `[!faq]-`：折叠细节推导/题解

---

### E. 模板化（_templates）让“持续纳入新书”变成低摩擦流程
#### E1. 创建模板文件（建议最小集）
在 `Content/_templates/` 下创建：
1. `note.section.md`（节笔记模板）
2. `note.chapter-summary.md`（章节汇总模板）
3. `track.index.md`（课程/书籍入口模板）
4. `wiki.concept.md`
5. `wiki.comparison.md`（可选：theorem/query 视你需求增补）

**Why**：确保你每次从书籍生成笔记时，结构一致、字段齐全；减少后续 Maintenance 的修复量。  
**How**：把 D 部分的 frontmatter 与固定章节结构写入模板，并包含：
- “相关笔记：[[前节]] | [[后节]]”
- “## 参见 Wiki”候选列表

---

### F. 工作流落地：Learn → Ingest → Maintenance（绑定 track）
#### F1. Learn（每学完一章/一讲执行）
对 `{Domain}/{track}/第N章`：
1. 生成该章所有节笔记到 `notes/{track}/第0N章…/`
2. 每篇节笔记必须：
   - frontmatter 字段完整
   - `相关笔记` 前后链接齐全
   - `## 参见 Wiki` 列出候选概念页链接
3. 创建/更新章节汇总：`第0N章 … — 章节汇总.md`
4. 更新 `tracks/{track}.md` 的进度与章节索引
5. 更新 `Content/{Domain}/index.md` 的统计信息

#### F2. Ingest（每完成一章后执行：从 Raw Notes 提炼 Wiki）
对该章所有节笔记：
1. 从 `## 参见 Wiki` 收集候选概念
2. 满足“跨章节/足够重要”的条目，创建到：
   - `concepts/`、`theorems/`、`comparisons/`、`queries/`
3. 对已存在概念页追加来源章节（建议用小节标题结构，如 `### {track} 第N章`）
4. 修复断链：优先 aliases + `[[文件名|显示名]]`
5. 更新索引（强制）：
   - `Content/Wiki/index.md`（新增行/计数）
   - `Content/{Domain}/index.md`（本域统计）
   - `Content/Wiki/log.md`（append ingest 记录）

#### F3. Maintenance（定期执行：输出 health 报告）
1. 断链检查：未解析链接、同名冲突链接
2. Frontmatter 完整性抽查：type/domain/tags/date + note 必须字段
3. 计数一致性：`Wiki/index` 表格行数 vs 实际目录文件数 vs Domain/index 统计
4. 输出 `Content/Wiki/health/YYYY-MM-DD.md` 并在 `log.md` 追加记录

---

## Verification Steps（验证/验收步骤）
### 1) 结构验收
1. 打开 `Content/index.md`：能进入 3 个 Domain。
2. 打开每个 `Content/{Domain}/index.md`：能进入至少 1 个 track（如已创建）。

### 2) 模板与字段验收（抽查）
每个 Domain 抽查至少：
- 2 篇节笔记（type=note）
- 2 个概念页（type=concept）
验证必填字段存在且格式统一：`title/type/domain/tags/date`；note 额外包含 `track/book/chapter/section`。

### 3) 链接验收
1. Obsidian 的“未解析链接 / Broken links”视图中，不应出现大规模断链。
2. 存在“显示名 ≠ 文件名”的链接必须采用 `[[文件名|显示名]]` 或 aliases 可解析。

### 4) 索引一致性验收
1. `Content/Wiki/index.md` 的各 Domain 四类表格行数与对应目录文件数量一致。
2. `Content/{Domain}/index.md` 的统计（笔记数/Wiki数）与实际一致。
3. 如不一致：按 Maintenance 产出 health 报告并修复，再复验。

---

## Executor Notes（执行提示：避免返工的操作建议）
1. 迁移/移动文件尽量在 Obsidian 内完成（它会自动更新多数链接）。
2. “数学”域建议先整体归档（如 `Content/_archive/数学/`）并在 SCHEMA 的 Domain 表标记为 `archived`，等新域稳定后再做精简抽取。
3. 一旦 SCHEMA 的目录/标签/命名规则确定，后续不要轻易变动；新增内容全部走模板与工作流。

