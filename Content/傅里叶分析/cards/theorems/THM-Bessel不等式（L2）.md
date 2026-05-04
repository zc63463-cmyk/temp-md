---
title: "THM-Bessel不等式（L2）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第03章"
tags:
  - 傅里叶分析/cards
  - theorem
  - L2
  - 正交展开
  - Bessel不等式
---

> [!abstract]
> $L^2(\mathbb T)$ 中正交展开的“能量不增”结论：Fourier 系数平方和不超过函数的 $L^2$ 能量。
>
# 可调用口径
- **结论**：对 $f\in L^2(\mathbb T)$，有 $\sum_{n\in\mathbb Z}|\widehat f(n)|^2\le \|f\|_2^2$。
- **适用条件**：只需要 $L^2$（Hilbert 空间结构）；不要求点态意义或额外光滑性。
- **含义**：频域“能量”不会超过时域能量；Fourier 系数必属 $\ell^2$。
- **常用用途**：用 $\|f\|_2$ 上界控制系数平方和；给出一类统一的先验估计。
- **对照**：把不等号升级为等号需要“完备性/稠密性”（见 Parseval）。
- **注意**：它不提供点态收敛结论（点态属于 3.2 的范畴）。

# 真源（勿在本卡重复维护）
![[3.1 Fourier级数的均方收敛#^pf-3-1-bessel]]

# 关联
- 章节：[[第03章 Fourier级数的收敛性 — 章节汇总]]｜[[第03章 Fourier级数的收敛性 — ingest(MOC)]]
- 上游：[[FML-L2内积（圆周归一化）]]｜[[FML-Fourier系数与部分和（定义）]]
- 下游：[[THM-Parseval恒等式（圆周Plancherel）]]
