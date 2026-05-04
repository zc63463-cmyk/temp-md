---
title: "第08章 Dirichlet定理 — 章节汇总"
type: chapter-summary
book: "Stein Fourier Analysis"
chapter: "第08章 Dirichlet定理"
tags:
  - 傅里叶分析
  - ChapterSummary
  - 数论
cssclasses:
  - wide-page
date: 2026-04-24
---

> [!abstract]
> 本章把“有限 Fourier（characters 的正交性）”带入解析数论：用 Dirichlet characters 把同余类条件线性化；用 Dirichlet $L$-函数的 Euler 乘积与在 $s=1$ 附近的解析性质，把“算术级数中素数无穷多”归结为“某些对数级数的发散/非消失”。核心是 **正交性 + 乘法结构（Euler 乘积）+ 解析延拓/非消失** 的协同。

^overview

## 全章结构图（主线）
```mermaid
flowchart TD
  A[8.1 数论准备<br/>Dirichlet character 与正交性<br/>L-函数与Euler乘积] --> B[8.2 Dirichlet定理<br/>从同余类到character平均<br/>主定理陈述与策略]
  B --> C[8.3 证明<br/>主特征的极点<br/>非主特征的L(1,χ)非零<br/>发散比较得到无穷多素数]
  C --> D[8.4 练习<br/>Euler模板与求和技巧]
  C --> E[8.5 问题<br/>显式计算L(1,χ)_因子函数]
```

## 各节要点（嵌入聚合）
- ![[8.1 一些基本的数论知识#^overview]]
- ![[8.2 Dirichlet定理#^overview]]
- ![[8.3 Dirichlet定理的证明#^overview]]
- ![[8.4 练习#^overview]]
- ![[8.5 问题#^overview]]

## 跨节接口（复用节点）
- **characters 的角色**：把“$n\equiv a\pmod q$”这类条件写成对 Dirichlet characters 的有限和（正交性给出 delta）。
- **主特征 vs 非主特征**：主特征对应的 $L$-函数包含 $\zeta(s)$ 的极点；非主特征需要证明 $L(1,\chi)\ne 0$，否则会破坏发散比较的结论。
- **Euler 乘积的适用域**：乘积与对数展开一般在 $\mathrm{Re}(s)>1$ 起步；后续把信息带到 $s\to 1^+$ 时要显式说明“哪一步仍合法”。
- **“看懂但不会用”的地方**：把“同余类素数”问题翻译成“对 $\sum_p p^{-s}$ 的加权和”的那一步，需要同时掌握：指示函数展开、Euler 乘积取对数、以及把错误项控制在有界量内。

## 本章索引
- 目录：[[index]]
- 章级入口：[[第08章 Dirichlet定理 — ingest(MOC)]]
- 节笔记：[[8.1 一些基本的数论知识]]、[[8.2 Dirichlet定理]]、[[8.3 Dirichlet定理的证明]]、[[8.4 练习]]、[[8.5 问题]]
