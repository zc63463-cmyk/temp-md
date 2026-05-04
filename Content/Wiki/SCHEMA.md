---
title: "SCHEMA — 算法 / 数据结构 / CPP 知识库构建规范"
type: schema
tags:
  - Wiki
  - 元数据
  - 规范
date: 2026-04-20
cssclasses:
  - wide-page
---

# SCHEMA — 算法 / 数据结构 / CPP 知识库构建规范

> [!abstract] 概览
> 本文件定义本 Obsidian 知识库的**唯一规范源**：目录结构、命名规则、标签层级、frontmatter 字段、以及 Learn → Ingest → Maintenance 三大工作流。  
> 目标是把原“数学”体系迁移为「算法 / 数据结构 / CPP」，并以**按课程/书籍（track）组织**为核心，保证长期可维护。

---

## 0. 核心决策（必须遵守）

1. **Domain（学科域）固定为 3 个**：`算法` / `数据结构` / `CPP`
2. **目录名使用 `CPP` 而非 `C++`**（跨平台与发布更稳定）；页面可用 `aliases: [C++]` 呈现显示名。
3. **索引手工维护为主**：不强依赖 Dataview 等插件（可选增强）。
4. **链接策略**：站内链接统一使用 `[[wikilinks]]`；显示名 ≠ 文件名时使用 `[[文件名|显示名]]` 或 `aliases`。

---

# 第一部分：架构定义

## 1. 四层内容模型（在 CS 场景下的解释）

```
┌─────────────────────────────────────────────────┐
│  导航层（Navigation）                             │
│  Content/index.md — 全库入口（Domain/Track 导航） │
│  Content/Wiki/index.md — 全局 Wiki 总目录          │
├─────────────────────────────────────────────────┤
│  Wiki 层（Knowledge Synthesis）                   │
│  {Domain}/concepts/      — 跨章节核心概念提炼       │
│  {Domain}/theorems/      — 重要定理/结论/性质        │
│  {Domain}/comparisons/   — 跨概念对比分析            │
│  {Domain}/queries/       — 常问问题与深度解答         │
├─────────────────────────────────────────────────┤
│  笔记层（Raw Notes）                              │
│  {Domain}/notes/{track}/ — 按课程/书籍、章节组织      │
│  {Domain}/canvas/{track}/— 可视化图谱（按节同步）      │
└─────────────────────────────────────────────────┘
```

> [!tip] 何时创建 Wiki 页？
> 当某个知识点**跨章节反复出现**、或需要跨书对比、或你希望形成“可复用解释”时，将其从 notes 提炼到 Wiki（concept/theorem/comparison/query）。

---

## 2. 目录结构（最终规范）

```
Content/
├── index.md                  # 全库首页（Domain/Track 导航）
├── Wiki/                     # 全局元数据（不放学科内容）
│   ├── SCHEMA.md             # 架构规范定义（本文件）
│   ├── index.md              # 全局 Wiki 总目录
│   ├── log.md                # 操作日志（append-only）
│   └── health/               # Lint/健康报告（Maintenance 产出）
│       └── YYYY-MM-DD.md
│
├── 算法/
│   ├── index.md
│   ├── tracks/               # 课程/书籍入口页
│   ├── concepts/
│   ├── theorems/
│   ├── comparisons/
│   ├── queries/
│   ├── notes/{track}/
│   │   ├── 第01章 {章标题}/
│   │   │   ├── {节号} {节标题}.md
│   │   │   └── 第01章 {章标题} — 章节汇总.md
│   │   └── ...
│   └── canvas/{track}/
│       └── ...
│
├── 数据结构/                 # 同上
├── CPP/                      # 同上（显示名用 aliases: [C++]）
│
├── _assets/                  # 全局静态资源（图片、附件等，可选）
└── _templates/               # 笔记模板（强烈建议）
```

---

## 3. 文件类型与定位（CS 适配）

| 类型 | 粒度 | 核心功能 | 创建时机 | 目录 |
|:-----|:-----|:---------|:---------|:-----|
| 节笔记 | 1节/1讲 | 完整记录 + 代码/例题 | 学完每节后 | `notes/{track}/` |
| 章节汇总 | 1章 | 章级复习 + 知识框架 | 学完每章后 | `notes/{track}/` |
| Track 入口 | 1书/1课 | 章节导航 + 进度 + Wiki 贡献 | 初始化/持续维护 | `tracks/` |
| Canvas | 1节 | 可视化知识图谱 | 与节笔记同步 | `canvas/{track}/` |
| 概念页 | 跨章节/跨书 | 可复用解释 | Ingest 时 | `concepts/` |
| 定理/性质页 | 跨章节 | 结论、证明要点、适用边界 | Ingest 时 | `theorems/` |
| 对比页 | 跨概念 | 易混淆点对照 | Query/复习时 | `comparisons/` |
| 常问问题页 | 跨章节 | 深度解答/总结 | Query 时 | `queries/` |

---

## 4. 命名规则（强约束）

| 类型 | 格式 | 示例 |
|:-----|:-----|:-----|
| 节笔记 | `{节号} {节标题}.md` | `3.2 线段树.md` / `Lecture-03 单调栈.md` |
| 章节汇总 | `第{N}章 {章标题} — 章节汇总.md` | `第03章 树结构 — 章节汇总.md` |
| Track 入口 | `{track}.md` | `CLRS.md` / `侯捷C++11.md` |
| Canvas | `{节号} {节标题}.canvas` | `3.2 线段树.canvas` |
| 概念页(英文/符号) | kebab-case | `std-vector.md` / `binary-search.md` |
| 概念页(中文) | 中文原名 | `线段树.md` |
| 对比页 | `{A}-vs-{B}.md` | `dp-vs-greedy.md` / `同构-vs-相似.md` |

> [!warning] 文件名禁忌
> - ❌ 不要在文件名中使用 `/`（Obsidian 会将其解释为路径分隔符）
> - ✅ 用 `_` 替代：如 `A_E_I_O 四种命题.md`

---

## 5. Domain 注册表（本库固定）

| 学科（显示） | 域名（目录名） | 创建日期 | 状态 |
|:--|:--|:--|:--|
| 算法 | 算法 | 2026-04-20 | active |
| 数据结构 | 数据结构 | 2026-04-20 | active |
| C++ | CPP | 2026-04-20 | active |
| 数学（原） | _archive/数学（建议） | 2026-04-20 | archived |

---

## 6. Tag Taxonomy（标签层级）

统一为：

```
#学习/{domain}/{子领域}/{关键词}
```

约束：
1. `domain ∈ {算法, 数据结构, CPP}`
2. `{子领域}` 尽量稳定（例如：DP / 图 / 树 / 堆 / STL / 并发）
3. `{关键词}` 可选，用于更细粒度定位

示例：
- `#学习/算法/DP/背包`
- `#学习/数据结构/树/线段树`
- `#学习/CPP/STL/vector`

---

# 第二部分：格式规范（frontmatter / 链接 / callouts）

## 7. Frontmatter（Properties）模板

### 7.1 节笔记（Raw Notes）
```yaml
---
title: "{节号} {节标题}"
type: note
domain: "{算法|数据结构|CPP}"
track: "{课程或书籍短名}"         # 例：CLRS / CP3 / 侯捷C++11
book: "{书名或课程名}"
chapter: "第{N}章 {章标题}"
section: "{节号或Lecture-XX}"
author: "{作者/讲者}"
source:
  - "{URL/ISBN/课程主页}"
tags:
  - "学习/{domain}/{子领域}/{关键词}"
aliases: []
date: 2026-04-20
cssclasses:
  - wide-page
---
```

### 7.2 概念页（Wiki: Concept）
```yaml
---
title: "{概念名}"
type: concept
domain: "{算法|数据结构|CPP}"
track: []
tags:
  - "学习/{domain}/{子领域}/{关键词}"
sources: []
related: []
date: 2026-04-20
---
```

### 7.3 对比页（Wiki: Comparison）
```yaml
---
title: "{A} vs {B}"
type: comparison
domain: "{算法|数据结构|CPP}"
tags:
  - "学习/{domain}/{子领域}/{关键词}"
related:
  - "[[{A}]]"
  - "[[{B}]]"
date: 2026-04-20
---
```

---

## 8. Wikilinks（内链）规范

1. 站内链接统一使用 `[[wikilinks]]`
2. 显示名 ≠ 文件名时，统一用：`[[文件名|显示名]]`
3. C++ 符号建议：
   - 文件名：`std-vector.md`
   - aliases：`[ "std::vector" ]`
   - 引用：`[[std-vector|std::vector]]`
4. 同名概念消歧（推荐）：文件名用括号标注域：如 `堆（数据结构）.md`、`堆（内存）.md`

---

## 9. Callouts（CS 场景语义）

- `[!abstract]`：一句话定位 + 要点列表（必须含 `==高亮==` 核心术语）
- `[!def]`：形式化定义（状态/不变式/复杂度/接口契约）
- `[!tip]`：套路/模板（DP 设计法、二分答案、单调栈模型等）
- `[!example]`：例题/代码（建议附 I/O 与关键注释）
- `[!warning]`：坑点（边界、溢出、UB、复杂度误判）
- `[!info]`：扩展（来源、变体、标准条款链接）
- `[!faq]-`：折叠的推导/题解细节

---

# 第三部分：工作流（Learn → Ingest → Maintenance）

## 10. Learn（每学完一章/一讲）

> [!check] Learn 产出清单
> - 节笔记：`notes/{track}/第0N章…/{节号} {节标题}.md`
> - 章节汇总：`notes/{track}/第0N章…/第0N章 … — 章节汇总.md`
> - Track 更新：`tracks/{track}.md` 更新进度与章节链接
> - Domain 首页更新：`{Domain}/index.md` 更新统计

每篇节笔记最小结构（建议）：
1. `[!abstract] 概览`
2. `## 知识结构图（mermaid）`
3. `## 核心内容（含 [!def]/[!tip]/[!example]/代码块）`
4. `## 易错点（[!warning]）`
5. `## 参见 Wiki（候选概念链接）`

---

## 11. Ingest（每完成一章后：从 notes 提炼 Wiki）

> [!check] Ingest 必做
> 1. 从该章节笔记 `## 参见 Wiki` 收集候选概念
> 2. 新建/补全 concepts/theorems/comparisons/queries
> 3. 修复断链与同名冲突（aliases 或 `[[文件名|显示名]]`）
> 4. 更新三处索引：`Wiki/index.md`、`{Domain}/index.md`、`Wiki/log.md`

---

## 12. Maintenance（定期：输出健康报告）

输出到：`Wiki/health/YYYY-MM-DD.md`

建议检查项：
1. 未解析链接（Broken links / unresolved）
2. frontmatter 完整性抽查（type/domain/tags/date + note 必须字段）
3. 索引一致性：Wiki/index 表格行数 vs 实际目录文件数 vs Domain/index 统计
4. 命名违规：文件名含 `/`、C++ 目录名不规范等

