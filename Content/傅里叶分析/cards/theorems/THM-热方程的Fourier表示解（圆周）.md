---
title: "THM-热方程的Fourier表示解（圆周）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第04章 4.4"
tags:
  - 傅里叶分析/cards
  - theorem
  - 热方程
  - 热核
  - Fourier方法
---

> [!abstract]
> 圆周热方程用 Fourier 模式对角化：每个频率独立按 $e^{-n^2 t}$ 衰减，从而得到显式级数解与核表示。
>
>
# 可调用口径
- **结论**：对 $2\pi$-周期初值 $f$，令 $u(x,t)=\sum_{n\in\mathbb Z}\widehat f(n)e^{-n^2 t}e^{inx}$，则对 $t>0$ 级数良好收敛并满足热方程（在适当意义下）。
- **关键一步**：$\partial_x^2 e^{inx}=-n^2 e^{inx}$，PDE 在频域变为 $c_n'(t)=-n^2 c_n(t)$。
- **平滑化机制**：$e^{-n^2 t}$ 对高频指数衰减，使 $t>0$ 时可逐项微分（级数与导数级数一致收敛）。
- **守恒量**：$n=0$ 模式不衰减，对应空间平均守恒。
- **对照**：与 Poisson 核（Abel）相比，热核对高频抑制更强，平滑更快。

# 真源（勿在本卡重复维护）
![[4.4 圆上的热方程#^prop-4-4-fourier-solution]]
![[4.4 圆上的热方程#^pf-4-4-fourier-solution]]

# 关联
- [[THM-热核是好核（t↓0回收初值）]]
- [[FML-热核H_t（定义与关键性质）]]

