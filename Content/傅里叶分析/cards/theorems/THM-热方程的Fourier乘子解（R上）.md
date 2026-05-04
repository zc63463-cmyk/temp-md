---
title: "THM-热方程的Fourier乘子解（R上）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第05章 5.2"
tags:
  - 傅里叶分析/cards
  - theorem
  - PDE
  - 热方程
  - 乘子
  - 核
---

> [!abstract]
> PDE 的标准模板：把微分算子对角化为频域乘子，再反演得到核表示（热核）。

# 可调用口径
- **结论**：对 $f\in\mathcal S(\mathbb R)$，热方程 $u_t=u_{xx}$ 的解可写为 $u(\cdot,t)=f*G_t$（$t>0$）。
- **频域表达**：$\widehat u(\xi,t)=e^{-(2\pi\xi)^2 t}\widehat f(\xi)$，即“每个频率独立指数衰减”。
- **用途**：一眼看出平滑化、衰减、以及 $t\downarrow 0$ 回收初值背后的机制（逼近恒等）。
- **关键合法性**：先在 $\mathcal S$ 上做，保证反演与逐项求导可交换；更弱函数类需额外工具。
- **常见误区**：漏掉 $2\pi$ 导致核的归一化常数错，从而破坏质量守恒 $\int G_t=1$。
- **复用方式**：以后遇到线性常系数 PDE，先写出对应乘子，再考虑反演与估计。

# 真源（勿在本卡重复维护）
![[5.2 偏微分方程中的一些应用#^thm-5-2-heat-solution]]
![[5.2 偏微分方程中的一些应用#^pf-5-2-heat-solution]]

# 关联
- 上游：[[THM-Fourier反演公式（R上）]]｜[[THM-Plancherel定理（R上）]]
- 下游：[[THM-Poisson求和公式]]（热核周期化的结构解释）
