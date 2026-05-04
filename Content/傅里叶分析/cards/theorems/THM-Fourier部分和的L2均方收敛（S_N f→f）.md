---
title: "THM-Fourier部分和的L2均方收敛（S_N f→f）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第03章"
tags:
  - 傅里叶分析/cards
  - theorem
  - L2
  - 均方收敛
  - 正交投影
  - Fourier部分和
---

> [!abstract]
> 在 $L^2(\mathbb T)$ 中，Fourier 部分和 $S_N f$ 是正交投影；随维数增大，投影逼近误差（尾部能量）趋于 0。
>
# 可调用口径
- **结论**：对任意 $f\in L^2(\mathbb T)$，有 $\|S_N f-f\|_2\to 0$（均方收敛）。
- **适用条件**：$L^2$ 足够；核心依赖 Parseval/完备性与正交投影分解。
- **含义**：$S_N$ 是“最佳均方逼近”；误差能量等于 Fourier 系数平方和的尾和。
- **常用用途**：把“收敛”转成“级数尾和趋 0”的代数事实，便于估计逼近误差。
- **对照**：均方收敛并不推出逐点收敛；点态需要 Dirichlet 核 + 正则性（3.2）。
- **注意**：这里的 $S_N$ 是硬截断投影；与 Fejér/Abel 的平滑平均不同（见第02章 2.5）。

# 真源（勿在本卡重复维护）
![[3.1 Fourier级数的均方收敛#^pf-3-1-l2-convergence]]

# 关联
- 章节：[[第03章 Fourier级数的收敛性 — 章节汇总]]｜[[第03章 Fourier级数的收敛性 — ingest(MOC)]]
- 上游：[[THM-Parseval恒等式（圆周Plancherel）]]｜[[FML-Fourier系数与部分和（定义）]]
- 对照：[[3.2 逐点收敛]]（点态收敛需要更强局部条件）
