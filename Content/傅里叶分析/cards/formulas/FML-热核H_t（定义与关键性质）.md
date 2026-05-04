---
title: "FML-热核H_t（定义与关键性质）"
type: card
card_type: formula
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第04章 4.4"
tags:
  - 傅里叶分析/cards
  - formula
  - 热核
  - Fourier乘子
---

> [!abstract]
> 圆周热核以频域乘子 $e^{-n^2 t}$ 定义：它同时编码了平滑化（高频强衰减）与逼近恒等（$t\downarrow 0$ 乘子趋于 1）。
>
>
# 可调用口径
- **定义**：$H_t(x)=\sum_{n\in\mathbb Z}e^{-n^2 t}e^{inx}$（对应频域乘子 $e^{-n^2 t}$）。
- **卷积表示**：$u(\cdot,t)=f*(2\pi)^{-1}H_t$ 给出热方程解（对 $t>0$）。
- **关键性质**：$t>0$ 时高频指数衰减 ⇒ 立即平滑；$t\downarrow 0$ 时 $H_t$ 形成逼近恒等（在归一化后）。
- **常用用途**：把 PDE 问题转成核估计/好核验收问题，并与 Poisson 核（Abel 平均）做对照。
- **注意**：若要直接看出正性/质量集中，通常会用 Poisson 求和把 $H_t$ 写成高斯核的周期化形式（本章提示即可，不在卡里展开推导）。

# 真源（勿在本卡重复维护）
![[4.4 圆上的热方程#^prop-4-4-fourier-solution]]
![[4.4 圆上的热方程#^prop-4-4-heat-kernel-good]]

# 关联
- [[THM-热核是好核（t↓0回收初值）]]
- [[THM-热方程的Fourier表示解（圆周）]]

