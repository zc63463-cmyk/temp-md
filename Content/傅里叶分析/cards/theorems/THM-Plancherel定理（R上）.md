---
title: "THM-Plancherel定理（R上）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第05章 5.1"
tags:
  - 傅里叶分析/cards
  - theorem
  - Fourier变换
  - L2
  - Plancherel
---

> [!abstract]
> 频域与时域在 $L^2$ 上等距：Fourier 变换是“能量守恒”的正交坐标变换。

# 可调用口径
- **结论（等距）**：$\|f\|_{2}=\|\widehat f\|_{2}$（按本章 $2\pi$ 约定）。
- **结论（内积保持）**：$\langle f,g\rangle=\langle \widehat f,\widehat g\rangle$，因此很多估计可直接在频域做。
- **适用范围**：先在 $\mathcal S(\mathbb R)$ 上证明，再以稠密性延拓到 $L^2(\mathbb R)$。
- **用途**：把微分算子变成乘子后，用 $L^2$ 等距给出稳定估计（PDE、乘子定理的底座）。
- **常见误区**：把“几乎处处反演”与“$L^2$ 反演/等距”混为一谈；二者技术门槛不同。
- **复用方式**：卡片只做入口；证明与细节以真源块为唯一可维护版本。

# 真源（勿在本卡重复维护）
![[5.1 Fourier变换的基本理论#^thm-5-1-plancherel]]
![[5.1 Fourier变换的基本理论#^pf-5-1-plancherel]]

# 关联
- 上游：[[THM-Fourier反演公式（R上）]]
- 下游：[[THM-热方程的Fourier乘子解（R上）]]｜[[THM-Heisenberg不确定性原理（Fourier形式）]]
