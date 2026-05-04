---
title: "FML-Bernoulli多项式 Fourier 展开"
type: card
card_type: formula
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第03章 3.4"
tags:
  - 傅里叶分析/cards
  - formula
  - Bernoulli多项式
  - Fourier展开
---

> [!abstract]
> Bernoulli 多项式在周期化后具有显式 Fourier 展开：它把“多项式 + 差分结构”与“Fourier 系数的幂衰减”直接连接起来。
>
>
# 可调用口径
- **结论（典型口径，$0<x<1$）**：$B_1(x)=x-\tfrac12=-\sum_{k\ne 0}\frac{e^{2\pi i k x}}{2\pi i k}$；且对 $n\ge 2$，$B_n(x)=-\frac{n!}{(2\pi i)^n}\sum_{k\ne 0}\frac{e^{2\pi i k x}}{k^n}$。
- **含义**：对 $n\ge 2$ 系数为 $1/k^n$ ⇒ 绝对收敛；$n=1$ 仅条件收敛（与 3.2 的点态/跳点口径一致）。
- **常用用途**：把 Bernoulli 对象与 $\zeta(2m)$、幂和公式、以及“特殊函数 Fourier 展开”的统一框架连起来。
- **注意**：该展开在区间内部成立；端点/跳点处要用左右极限平均解释。
- **外部对照**：NIST DLMF §24.8 列出 Bernoulli 多项式的 Fourier series。

# 真源（勿在本卡重复维护）
![[3.4 问题#^pf-3-4-05e]]

# 关联
- 对照来源：https://dlmf.nist.gov/24.8
- 上游：[[FML-ζ(2m) 与 Bernoulli 数]]

