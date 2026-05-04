---
title: "第08章 Dirichlet定理 — ingest(MOC)"
type: chapter-ingest
book: "Stein Fourier Analysis"
chapter: "第08章 Dirichlet定理"
tags:
  - 傅里叶分析
  - 傅里叶-强度
  - ChapterIngest
  - MOC
  - 数论
cssclasses:
  - wide-page
date: 2026-04-24
---

> [!abstract]
> 本章把有限 Fourier 分析的“characters 正交性”升级为解析数论工具：用 Dirichlet characters 对同余类做谱分解；用 $L$-函数与 Euler 乘积把素数信息编码为解析对象；最终用 $s\to 1^+$ 的发散/非消失比较推出 Dirichlet 定理。

^overview

## 0. 导航
- 章节汇总：[[第08章 Dirichlet定理 — 章节汇总]]
- 节笔记：[[8.1 一些基本的数论知识]]｜[[8.2 Dirichlet定理]]｜[[8.3 Dirichlet定理的证明]]｜[[8.4 练习]]｜[[8.5 问题]]
- 上游回链（去重）：[[7.2 有限Abel群上的Fourier分析]]（characters/正交性）｜[[7.4 问题#^faq-7-4-01]]（中国剩余）

> [!note] 去重策略声明（全库）
> - 第07章维护“有限 Abel 群上的 Fourier 闭环”（正交性/反演/卷积）；第08章只维护新增的“数论对象（Dirichlet character 与 L-函数）+ Dirichlet 定理证明主线”。
> - 证明/公式的唯一可维护真源固定在 8.1–8.3 节笔记中的 `^def-8-*` / `^lem-8-*` / `^thm-8-*` / `^pf-8-*` block-id。
> - cards 仅转引真源 block-id，不复制证明正文。
<!-- callout-break -->
> [!faq]- 完备证明入口（去重版）
> - 8.1 带余除法：[[8.1 一些基本的数论知识#^pf-8-1-euclid-division]]
> - 8.1 Bezout：[[8.1 一些基本的数论知识#^pf-8-1-bezout]]
> - 8.1 算术基本定理：[[8.1 一些基本的数论知识#^pf-8-1-fta]]
> - 8.1 Euler 乘积（zeta）：[[8.1 一些基本的数论知识#^pf-8-1-euler-product-zeta]]
> - 8.1 $\sum_p 1/p$ 发散：[[8.1 一些基本的数论知识#^pf-8-1-sum-1-over-p-diverges]]
> - 8.2 正交性：[[8.2 Dirichlet定理#^pf-8-2-orthogonality]]
> - 8.2 指示函数展开：[[8.2 Dirichlet定理#^pf-8-2-indicator-expansion]]
> - 8.2 Euler 乘积（L）：[[8.2 Dirichlet定理#^pf-8-2-euler-product-L]]
> - 8.2 主特征分解：[[8.2 Dirichlet定理#^pf-8-2-principal-zeta]]
> - 8.3 $\log_1$ 性质：[[8.3 Dirichlet定理的证明#^pf-8-3-log1-properties]]
> - 8.3 $\log L$ 主项：[[8.3 Dirichlet定理的证明#^pf-8-3-logL-main]]
> - 8.3 $L(1,\chi)$ 收敛：[[8.3 Dirichlet定理的证明#^pf-8-3-L1-converges]]
> - 8.3 非主特征非消失：[[8.3 Dirichlet定理的证明#^pf-8-3-nonvanishing]]
> - 8.3 Dirichlet 定理（主证明）：[[8.3 Dirichlet定理的证明#^pf-8-3-dirichlet]]

## 1. 本章 cards（去重入口）
- [[OBJ-Dirichlet特征（mod q）]]
- [[OBJ-Dirichlet L函数（定义_Euler乘积）]]
- [[FML-Dirichlet特征正交关系（mod q）]]
- [[FML-同余类指示函数的character展开]]
- [[THM-Dirichlet定理（算术级数素数无穷多）]]
- [[THM-非主特征L(1,χ)非零]]
- [[THM-主特征与s=1极点的角色]]
- [[MTH-Euler乘积对数化与发散比较（Dirichlet证明主线）]]

# 2. 外部参考（章级；附访问日期）
- MIT 18.785 Lecture Notes（Dirichlet characters 与 Dirichlet 定理）：https://math.mit.edu/classes/18.785/2018fa/LectureNotes18.pdf （访问：2026-04-24）
- Wikipedia：Dirichlet L-function：https://en.m.wikipedia.org/wiki/Dirichlet_L-function （访问：2026-04-24）
- Wikipedia：Dirichlet's theorem on arithmetic progressions：https://en.m.wikipedia.org/wiki/Dirichlet%27s_theorem_on_arithmetic_progressions （访问：2026-04-24）
- Soundararajan notes（Dirichlet theorem proof outline）：http://math.stanford.edu/~ksound/Math155W10/Dirichlet3.pdf （访问：2026-04-24）
