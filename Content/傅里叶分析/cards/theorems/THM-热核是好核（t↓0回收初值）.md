---
title: "THM-热核是好核（t↓0回收初值）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第04章 4.4"
tags:
  - 傅里叶分析/cards
  - theorem
  - 好核
  - 热核
  - 逼近恒等
---

> [!abstract]
> 把热核归一化后得到一族好核：因此当 $t\downarrow 0$，卷积 $f*K_t$ 在连续意义下一致回收初值，在 $L^1$ 意义下于 Lebesgue 点回收。
>
>
# 可调用口径
- **结论**：令 $K_t=(2\pi)^{-1}H_t$，则 $\{K_t\}$ 满足好核条件，故 $f*K_t\to f$（连续时一致；一般 $L^1$ 时在 Lebesgue 点处点态）。
- **验证口径**：归一化（质量为 1）+ $L^1$ 可控（非负且质量为 1）+ 质量集中（$t\downarrow 0$ 把质量推向 0 邻域）。
- **意义**：把“PDE 解的极限回收”转为“好核逼近恒等”的验收问题。
- **注意**：$t\downarrow 0$ 的极限不是形式推导，而是靠好核条件保证；否则卷积核可能不回收。
- **对照**：Poisson 核也是好核（第02章 2.5），但热核的频域衰减更强（$e^{-n^2 t}$）。

# 真源（勿在本卡重复维护）
![[4.4 圆上的热方程#^prop-4-4-heat-kernel-good]]
![[4.4 圆上的热方程#^pf-4-4-heat-kernel-good]]

# 关联
- [[THM-好核逼近定理]]
- [[THM-热方程的Fourier表示解（圆周）]]

