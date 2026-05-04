---
title: "THM-导数在L2则Fourier级数绝对收敛"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第03章 3.3"
tags:
  - 傅里叶分析/cards
  - theorem
  - 绝对收敛
  - CauchySchwarz
  - Parseval
---

> [!abstract]
> 一个典型“把 $\ell^2$ 推成 $\ell^1$”的门票：若 $f'\in L^2$，则 Fourier 系数满足 $\sum|\widehat f(n)|<\infty$，从而 Fourier 级数绝对（并一致）收敛。
>
>
# 可调用口径
- **结论**：若 $f$ 为 $2\pi$-周期且 $f'\in L^2(\mathbb T)$，则 $\sum_{n\in\mathbb Z}|\widehat f(n)|<\infty$。
- **关键等式**：Parseval 应用于导数：$\sum n^2|\widehat f(n)|^2=\|f'\|_2^2$。
- **关键技巧**：写成 $\sum_{n\ne 0}|\widehat f(n)|=\sum (1/|n|)\cdot |n\widehat f(n)|$，再用 Cauchy–Schwarz。
- **常用用途**：给出“足够正则性 ⇒ Fourier 级数绝对/一致收敛”的标准路径（比仅 $L^2$ 强很多）。
- **注意**：需要处理 $n=0$ 项（常数项）并选择正确权重 $1/n$（最易写错）。

# 真源（勿在本卡重复维护）
![[3.3 练习#^pf-3-3-14]]

# 关联
- 对照：[[THM-Fourier部分和的L2均方收敛（S_N f→f）]]（仅 $L^2$ 结论）

