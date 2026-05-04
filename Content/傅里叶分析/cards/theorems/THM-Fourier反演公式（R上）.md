---
title: "THM-Fourier反演公式（R上）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第05章 5.1"
tags:
  - 傅里叶分析/cards
  - theorem
  - Fourier变换
  - 反演
---

> [!abstract]
> 频域计算闭环的“回到时域”接口：把 $\widehat f$ 重新还原成 $f$。

# 可调用口径
- **结论**：在本章约定下，$f(x)=\int_{\mathbb R}\widehat f(\xi)e^{2\pi i x\xi}d\xi$（在合适意义下成立）。
- **典型充分条件**：$f\in\mathcal S(\mathbb R)$；或 $f,\widehat f\in L^1(\mathbb R)$（点态/几乎处处版本按教材口径选用）。
- **用途**：把“乘子/估计”从频域搬回时域（PDE、核表示、Poisson 求和、不确定性都依赖它）。
- **常见误区**：忽略常数约定（$2\pi$）会导致后续核与不等式常数整体错位。
- **配套工具**：卷积定理与近似恒等（用来解释极限交换与回收初值）。
- **复用方式**：只引用真源块；不要在卡片里重复维护证明正文。

# 真源（勿在本卡重复维护）
![[5.1 Fourier变换的基本理论#^thm-5-1-inversion]]
![[5.1 Fourier变换的基本理论#^pf-5-1-inversion]]

# 关联
- 章节：[[第05章 R上的Fourier变换 — ingest(MOC)]]｜[[第05章 R上的Fourier变换 — 章节汇总]]
- 下游：[[THM-Plancherel定理（R上）]]｜[[THM-热方程的Fourier乘子解（R上）]]｜[[THM-Poisson求和公式]]
