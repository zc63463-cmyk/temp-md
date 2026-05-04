---
title: "Obsidian-Book-KB 使用说明"
date: 2026-04-20
---

# Obsidian-Book-KB（本地读书知识库骨架）

你现在拿到的是一个**可直接作为 Obsidian Vault 打开的目录骨架**，已经包含：

- `Content/`：知识库正文（首页、Wiki 元数据、学科占位符、模板、附件）
- `Content/Wiki/SCHEMA.md`：规范真源（你上传的模板已完整落地）
- `Content/_templates/`：节笔记/章节汇总/概念页/对比页/索引/日志/日记模板
- `Content/学科-占位符/`：示例学科目录（可重命名）
- `00-Inbox/`：快速捕获
- `00-Raw素材/`：原始素材（PDF/截图/课件等）

---

## 1) 在 Windows 打开为 Vault

1. 打开 Obsidian
2. **Open folder as vault**（将本文件夹作为 Vault 打开）

---

## 2) 必做设置（避免后期炸链/散附件）

在 Obsidian Settings 中：

### Files & Links
- 开启：**自动更新内部链接**
- 新链接格式：**Shortest path（最短路径）**

### Files & Links → Attachments
- 附件默认位置：`Content/_assets/`
- 图片粘贴：复制到附件文件夹（不要散落在章目录）

---

## 3) 建议安装的社区插件（最小可用集）

> 你可以先装最少集，后续再扩展。

- **Templater**：模板自动化（生成节笔记/概念页等）
- **Dataview**：索引与统计（学科首页、概念清单等）
- **Linter**：格式一致性（frontmatter/空行/标题等）
- **Calendar + Periodic Notes**（可选）：日记流
- **QuickAdd**（强烈建议）：把“新建节笔记/概念页/对比页”做成快捷动作

---

## 4) 你要改的 3 件事（从占位符到可用）

1. 把 `Content/学科-占位符/` 重命名为你的真实学科名（例如 `线性代数` 或 `LADR`）
2. 在 `Content/学科名/index.md` 里把 `{书名}/{作者}/{版次}` 等占位符替换成真实信息
3. 用 `Content/_templates/` 里的模板开始写第一章，并在 `Content/Wiki/SCHEMA.md` 里回填“标杆文件路径”

---

## 5) 验收清单（打开后 5 分钟自检）

- [ ] 能正常打开 Vault
- [ ] 在 `Content/index.md` 中能点开：`Wiki/SCHEMA`、`Wiki/index`、`Wiki/log`、学科首页
- [ ] 新建两篇测试笔记互链后重命名其中一篇，链接会自动更新
- [ ] 粘贴图片后，图片会进入 `Content/_assets/`
- [ ] 模板能直接套用生成一篇节笔记，并且 callout/mermaid 能正常渲染

