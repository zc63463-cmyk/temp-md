---
title: "第07章 有限Fourier分析 — ingest(MOC)"
type: chapter-ingest
book: "Stein Fourier Analysis"
chapter: "第07章 有限Fourier分析"
tags:
  - 傅里叶分析
  - 傅里叶-强度
  - ChapterIngest
  - MOC
cssclasses:
  - wide-page
date: 2026-04-24
---

> [!abstract]
> 本章主线（去重版）：在 $Z_N$ 与一般有限 Abel 群上建立 Fourier 分析的“正交基—系数—反演/Plancherel—卷积定理”闭环，并把它当成离散的有限维 Hilbert 空间分解工具，用于后续计数/和式估计与算法直觉。

^overview

## 0. 导航
- 章节汇总：[[第07章 有限Fourier分析 — 章节汇总]]
- 节笔记：[[7.1 Z_N上的Fourier分析]]｜[[7.2 有限Abel群上的Fourier分析]]｜[[7.3 练习]]｜[[7.4 问题]]
- 上游回链（去重）：[[2.2 Fourier级数的唯一性]]｜[[2.3 卷积]]｜[[5.3 Poisson求和公式]]

> [!note] 去重策略声明（全库）
> - 第07章把“有限维/离散”的 Fourier 分析作为独立真源；与第05/06章的连续 Fourier 区分维护，避免常数/测度混淆。
> - 证明/公式的唯一可维护真源固定在节笔记中的 `^thm-7-*` / `^pf-7-*` 以及少量 `^def-7-*` block-id。
> - cards 仅转引真源 block-id，不复制证明正文。
<!-- callout-break -->
> [!faq]- 完备证明入口（去重版）
> - 7.1 正交性：[[7.1 Z_N上的Fourier分析#^pf-7-1-orthogonality]]
> - 7.1 反演：[[7.1 Z_N上的Fourier分析#^pf-7-1-inversion]]
> - 7.1 Plancherel：[[7.1 Z_N上的Fourier分析#^pf-7-1-plancherel]]
> - 7.1 卷积定理：[[7.1 Z_N上的Fourier分析#^pf-7-1-convolution]]
> - 7.2 对偶群基础：[[7.2 有限Abel群上的Fourier分析#^pf-7-2-dual-basics]]
> - 7.2 反演：[[7.2 有限Abel群上的Fourier分析#^pf-7-2-inversion]]
> - 7.2 Plancherel：[[7.2 有限Abel群上的Fourier分析#^pf-7-2-plancherel]]
> - 7.2 卷积定理：[[7.2 有限Abel群上的Fourier分析#^pf-7-2-convolution]]

## 1. 本章 cards（去重入口）
- [[THM-Z_N上Fourier反演公式]]
- [[THM-Z_N上Plancherel（Parseval）]]
- [[THM-有限Abel群上Fourier反演公式]]
- [[THM-有限Abel群上Plancherel（Parseval）]]
- [[FML-字符正交关系（有限群）]]
- [[FML-有限群卷积定理（卷积_点乘）]]
- [[OBJ-有限Abel群的character与对偶群]]
- [[MTH-用正交性计算有限和（Fourier trick）]]

# 2. 外部参考（用于“补充理解与易混淆点”；附访问日期）
- Tao：Finite abelian groups 的 Fourier 分析讲义（characters/正交性/反演/Plancherel）：https://www.math.ucla.edu/~tao/247b.1.07w/notes9.pdf （访问：2026-04-24）
- Babai：Fourier Transform and Equations over Finite Abelian Groups：https://people.cs.uchicago.edu/~laci/HANDOUTS/fourier.pdf （访问：2026-04-24）
- Fourier transform on finite groups（定义与符号对照）：https://en.m.wikipedia.org/wiki/Fourier_transform_on_finite_groups （访问：2026-04-24）
- 课程笔记（符号/例子对照，可选）：https://danielnaylor.uk/notes/III/Michaelmas/AC/HTML/ACse2.html （访问：2026-04-24）
