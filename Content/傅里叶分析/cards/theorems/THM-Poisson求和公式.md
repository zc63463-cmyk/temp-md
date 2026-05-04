---
title: "THM-Poisson求和公式"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第05章 5.3"
tags:
  - 傅里叶分析/cards
  - theorem
  - Fourier变换
  - Poisson求和
  - 晶格
---

> [!abstract]
> “离散求和 = 频域采样”：把整数点求和与 Fourier 变换在整数频率处的取值精确连接起来。

# 可调用口径
- **结论（Schwartz 版）**：对 $f\in\mathcal S(\mathbb R)$，有 $\sum_{n\in\mathbb Z} f(n)=\sum_{k\in\mathbb Z}\widehat f(k)$（按本章 $2\pi$ 约定）。
- **用途**：把离散问题转成连续估计（或反过来）；是“周期化/取样/晶格”结构的核心桥梁。
- **典型推法**：从周期化函数的 Fourier 系数出发，或用分布/对偶性写成同一恒等式的两种展开。
- **常见误区**：对收敛与交换次序掉以轻心；必须先在 $\mathcal S$（或足够衰减/光滑）上成立。
- **下游连接**：可导出 Jacobi θ 变换、估计整数点和、以及数论中的基本公式。
- **复用方式**：只转引真源块；当需要改常数约定时，只改节笔记真源。

# 真源（勿在本卡重复维护）
![[5.3 Poisson求和公式#^thm-5-3-poisson-summation]]
![[5.3 Poisson求和公式#^pf-5-3-poisson-summation]]

# 关联
- 上游：[[THM-Fourier反演公式（R上）]]
- 下游：[[THM-Heisenberg不确定性原理（Fourier形式）]]（高斯与极值常与 Poisson 同时出现）
