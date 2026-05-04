---
title: "知识库操作日志"
type: log
tags:
  - Wiki
  - 元数据
date: YYYY-MM-DD
cssclasses:
  - wide-page
---

# 操作日志

> [!info] 说明
> 本日志采用 **append-only** 模式，所有知识库变更必须记录。禁止修改或删除已有条目。相关文件：[[Wiki/SCHEMA]] | [[index]]

## Action 类型一览

| Action | 含义 |
|:-------|:-----|
| `init` | 初始化 |
| `create` | 创建页面 |
| `enrich` | 充实内容 |
| `restructure` | 结构调整 |
| `lint` | 链接/格式检查 |
| `audit` | 全面审计 |
| `fix` | 修复问题 |
| `ingest` | 知识编译（批量） |
| `query` | 查询结果回写 |
| `compare` | 创建对比页 |
| `contradiction` | 标记矛盾 |

---

## [YYYY-MM-DD] init | 知识库
- 初始化知识库目录结构
- 创建 Wiki 元数据文件：SCHEMA.md、index.md、log.md
- 创建所有笔记模板文件
- 创建首页 Content/index.md

## [YYYY-MM-DD] init | {学科}
- 创建学科目录 Content/{学科}/（concepts/、theorems/、comparisons/、queries/、notes/、canvas/）
- 编写学科 index.md
- 更新 Wiki/index.md、Wiki/SCHEMA.md、Content/index.md

