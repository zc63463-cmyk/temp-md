---
title: "OBJ-有限Abel群的character与对偶群"
type: card
card_type: object
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第07章 7.2"
tags:
  - 傅里叶分析/cards
  - object
  - finite-fourier
  - abelian-group
  - character
  - dual-group
---

> [!abstract]
> 在有限 Abel 群 $G$ 上，character $\chi:G\to S^1$ 是“指数函数”的抽象化；所有 characters 组成对偶群 $\widehat G$，它是 Fourier 变换的频域空间。

# 可调用口径
- character 是 1 维表示：$\chi(xy)=\chi(x)\chi(y)$，且 $|\chi(x)|=1$。
- 对偶群 $\widehat G$：所有 characters，按点乘构成有限 Abel 群。
- 频域变量不是 $G$ 本身，而是 $\widehat G$；只有在选定分解时才可与 $G$ 具体同构。
- 典型用途：把 $f:G\to\mathbb C$ 展开为 characters 的线性组合，从而做反演/Plancherel/卷积对角化。

# 真源（勿在本卡重复维护）
![[7.2 有限Abel群上的Fourier分析#^def-7-2-conventions]]

