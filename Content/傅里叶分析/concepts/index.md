---
title: "傅里叶分析｜concepts 索引"
type: concepts-index
tags:
  - 傅里叶分析
  - 导航
  - concepts
  - MOC
date: 2026-04-25
cssclasses:
  - wide-page
---

> [!abstract] 用法
> 这里汇总傅里叶分析学科下的 **concepts 概念页**，按主线主题分组。  
> 原则：concepts 只给“可复用定义/性质/误区 + 真源回链”；完整证明仍在 notes 真源块维护。
^overview

## 完成度标准（从 stub 到可复用）
> [!note] 约定
> - concepts 负责“可复用的知识节点”；notes 负责“长推导/证明真源”；cards 负责“可调用入口”。
> - 公式与排版必须天然满足门禁：不使用 LaTeX 换行符、不要使用 begin/end 环境，display 仅用单行 `$$...$$`。
>
> **达到以下条件即可移除 `stub` 标签（或改为 `status: mature`）：**
> 1) 存在 `^overview`（独立行）。  
> 2) “一句话定位”能说明其在本书链条中的角色。  
> 3) 至少 2 条真源回链：**notes 真源**（章/节）+ **cards 入口**（theorem/method/formula/object）各 1 条。  
> 4) 最少包含 3 个模块：**定义**、**关键性质（表格或条目）**、**常见误区**。  
> 5) 若涉及极限口径，明确写出“连续点 / Lebesgue 点 / 跳点左右平均”等适用条件。

## 重定向规范（别名/重音符/旧链接）
> [!warning] 只允许一个 canonical 内容页
> 对同一概念的不同文件名（例如重音符差异、中文别名）：
> - 选定一个 canonical 页维护正文；
> - 其它页只保留极短说明并指向 canonical（避免出现两份“真源”导致漂移）。
>
> 提示：可用 `scan_notes.py --check-duplicates` 发现弱归一化同名风险。

## A. 核与求和法（坏核→好核）
- [[Content/傅里叶分析/concepts/Dirichlet核]]
- [[Content/傅里叶分析/concepts/Fejer核]]
- [[Content/傅里叶分析/concepts/Poisson核]]
- [[Content/傅里叶分析/concepts/Cesaro平均]]
- [[Content/傅里叶分析/concepts/Abel平均]]
- [[Content/傅里叶分析/concepts/好核（逼近恒等）]]
- [[Content/傅里叶分析/concepts/坏核修正为好核]]

## B. 卷积语言（把级数写成核）
- [[Content/傅里叶分析/concepts/圆周卷积]]
- [[Content/傅里叶分析/concepts/卷积（圆周）]]（兼容入口）
- [[Content/傅里叶分析/concepts/频域点乘原理]]
- [[Content/傅里叶分析/concepts/核化思想]]
- [[Content/傅里叶分析/concepts/把级数写成核]]

## C. 收敛与门槛（L2 / 点态）
- [[Content/傅里叶分析/concepts/L2圆周空间]]
- [[Content/傅里叶分析/concepts/指数正交系]]
- [[Content/傅里叶分析/concepts/Hilbert空间正交展开]]
- [[Content/傅里叶分析/concepts/能量法视角]]
- [[Content/傅里叶分析/concepts/左右极限]]
- [[Content/傅里叶分析/concepts/有界变差函数（BV）]]
- [[Content/傅里叶分析/concepts/对称化技巧]]
- [[Content/傅里叶分析/concepts/Lebesgue点]]

## D. PDE 接口
- [[Content/傅里叶分析/concepts/热方程]]
- [[Content/傅里叶分析/concepts/波动方程]]
- [[Content/傅里叶分析/concepts/Laplacian]]
- [[Content/傅里叶分析/concepts/分离变量法]]
- [[Content/傅里叶分析/concepts/守恒律推导PDE]]
- [[Content/傅里叶分析/concepts/坐标适配]]
- [[Content/傅里叶分析/concepts/Fourier展开（周期边界）]]

## E. 复数工具（第01章常用）
- [[Content/傅里叶分析/concepts/复数]]
- [[Content/傅里叶分析/concepts/复共轭]]
- [[Content/傅里叶分析/concepts/复指数]]
- [[Content/傅里叶分析/concepts/指数化技巧（Euler）]]
