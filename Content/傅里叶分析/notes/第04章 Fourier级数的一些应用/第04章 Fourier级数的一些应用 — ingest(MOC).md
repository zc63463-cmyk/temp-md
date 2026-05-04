---
title: "第04章 Fourier级数的一些应用 — ingest(MOC)"
type: chapter-ingest
book: "Stein Fourier Analysis"
chapter: "第04章 Fourier级数的一些应用"
tags:
  - 傅里叶分析
  - 傅里叶-强度
  - ChapterIngest
  - MOC
date: 2026-04-23
cssclasses:
  - wide-page
---

> [!abstract]
> 本章主线（去重版）：把几何/数论/病态现象/PDE 统一翻译成 Fourier 语言——将结构性问题化为频域系数的可控估计（Parseval/不等式/核方法/指数和），再用“真源证明块”与 cards 做可复用入口。
>
^overview

## 0. 导航
- 章节汇总：[[第04章 Fourier级数的一些应用 — 章节汇总]]
- 节笔记：[[4.1 等周不等式]]｜[[4.2 Weyl等分布定理]]｜[[4.3 处处不可微的连续函数]]｜[[4.4 圆上的热方程]]
- 上游权威条目（去重回链）：[[3.1 Fourier级数的均方收敛]]｜[[3.2 逐点收敛]]｜[[2.4 好核]]｜[[2.5 Cesaro和Abel求和]]

> [!note] 去重策略声明（全库）
> - 第04章偏“应用章”：当使用到核/好核/卷积的通用口径时，优先回链第02章（2.4/2.5）真源，不在本章重复维护抽象理论。
> - 本章每节的 proof 以 `^pf-4-*` 作为唯一可维护真源；cards 仅转引 block-id，不复制证明正文。
<!-- callout-break -->
> [!faq]- 完备证明入口（去重版）
> - 4.1 等周不等式：[[4.1 等周不等式#^pf-4-1-isoperimetric]]
> - 4.2 Weyl（2⇒1）：[[4.2 Weyl等分布定理#^pf-4-2-weyl-2to1]]
> - 4.2 Weyl（1⇒2）：[[4.2 Weyl等分布定理#^pf-4-2-weyl-1to2]]
> - 4.2 无理旋转等分布：[[4.2 Weyl等分布定理#^pf-4-2-irrational-rotation]]
> - 4.3 Weierstrass 处处不可微：[[4.3 处处不可微的连续函数#^pf-4-3-weierstrass]]
> - 4.4 热方程 Fourier 表示解：[[4.4 圆上的热方程#^pf-4-4-fourier-solution]]
> - 4.4 热核是好核：[[4.4 圆上的热方程#^pf-4-4-heat-kernel-good]]
>
## 1. 本章 cards（去重入口）
- 定理：
  - [[THM-等周不等式（Fourier证明）]]
  - [[THM-Weyl判别准则（等分布⇔指数和）]]
  - [[THM-无理旋转等分布（nα）]]
  - [[THM-Weierstrass处处不可微（疏频）]]
  - [[THM-热方程的Fourier表示解（圆周）]]
  - [[THM-热核是好核（t↓0回收初值）]]
- 公式/方法：
  - [[FML-热核H_t（定义与关键性质）]]
  - [[MTH-尺度选择法（lacunary主频支配）]]

# 2. 外部参考（用于“补充理解与易混淆点”callout；附访问日期）
- 等周不等式（Fourier/Parseval 证明口径）
  - https://courses.cs.washington.edu/courses/cse533/05wi/lectures/lect04.pdf （访问：2026-04-23）
  - https://www.math.cuhk.edu.hk/course_builder/2122/math3093/Feb%2024%20Fourier.pdf （访问：2026-04-23）
- Weyl 等分布
  - https://krex.k-state.edu/dspace/bitstream/2097/40841/1/RachelAndriunas2020.pdf （访问：2026-04-23）
- Weierstrass 处处不可微
  - https://live.ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/mit18_100af20_lec18.pdf （访问：2026-04-23）
  - https://www2.math.upenn.edu/~gressman/analysis/09-nowhere.html （访问：2026-04-23）
- 热方程/热核/Poisson 求和
  - https://www.ceremade.dauphine.fr/~mischler/UHcrash/UHcrash1.pdf （访问：2026-04-23）
  - https://en.m.wikipedia.org/wiki/Poisson_summation_formula （访问：2026-04-23）
