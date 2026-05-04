---
title: "OBJ-缓降函数（R_d反常积分接口）"
type: card
card_type: object
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第09章 9.3"
tags:
  - 傅里叶分析/cards
  - object
  - integration
  - improper-integral
  - slowly-decreasing
---

> [!abstract]
> “缓降函数”是一类在无穷远衰减足够快的连续函数，使得 $R^d$ 上的积分可以用截断极限定义，并且可稳定地做换序与卷积型积分操作（为 Fourier 变换做准备）。

# 可调用口径
- 定义：存在 $A$ 使 $|f(x)|\le A/(1+|x|^{d+1})$。
- 结论：$\int_{R^d}f$ 可由 $\int_{[-N,N]^d}f$ 的极限定义，且与球截断等常见方式一致。
- 典型用途：确保反常积分存在、允许把卷积/换序写成可复用等式。

# 真源（勿在本卡重复维护）
![[9.3 反常积分 R_d上的积分#^def-9-3-slowly-decreasing]]
![[9.3 反常积分 R_d上的积分#^thm-9-3-existence]]
![[9.3 反常积分 R_d上的积分#^pf-9-3-existence]]

