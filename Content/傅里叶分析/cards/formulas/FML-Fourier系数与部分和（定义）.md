---
title: "FML-Fourier系数与部分和（定义）"
type: card
card_type: formula
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第03章"
tags:
  - 傅里叶分析/cards
  - formula
  - Fourier系数
  - Fourier部分和
  - 正交投影
---

> [!abstract]
> 在 $L^2(\mathbb T)$ 视角中，Fourier 系数是正交投影坐标；部分和 $S_N f$ 是到有限维指数子空间的正交投影。
>
# 可调用口径
- **Fourier 系数**：$\widehat f(n)=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(x)e^{-inx}\,dx$（与内积归一化一致）。
- **部分和**：$S_N f(x)=\sum_{|n|\le N}\widehat f(n)e^{inx}$（到低频子空间的正交投影）。
- **含义**：$S_N$ 不是“平均平滑”，而是“硬截断投影”（在 $L^2$ 下是最佳逼近）。
- **常用用途**：$L^2$ 理论中把逼近误差写成尾部能量；点态理论中把 $S_N$ 改写成卷积核积分。
- **对照**：同一算子也可写成 $S_N f=f*D_N$（完整证明真源在第02章 2.3）。
- **注意**：点态收敛讨论时要面对 Dirichlet 核的振荡与奇异性（3.2）。

# 真源（勿在本卡重复维护）
![[3.1 Fourier级数的均方收敛#^def-3-1-fourier-coeff]]
![[3.1 Fourier级数的均方收敛#^def-3-1-partial-sum]]

# 关联
- [[THM-Fourier部分和的L2均方收敛（S_N f→f）]]
- 对照：[[FML-部分和=卷积（Dirichlet核）]]（同一算子在核语言中的表达）
