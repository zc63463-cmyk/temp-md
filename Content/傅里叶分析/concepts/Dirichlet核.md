---
title: "Dirichlet核"
type: concept
tags:
  - 傅里叶分析
  - concept
date: 2026-04-24
cssclasses:
  - wide-page
status: mature
---

> [!abstract] 定位（一句话）
> Dirichlet 核 $D_N$ 是 Fourier **部分和算子** $S_N f$ 的卷积核（因此决定了点态收敛问题的“振荡/奇异性”）。
^overview

## 真源回链（先止血）
- 公式（部分和 = 卷积）：[[Content/傅里叶分析/cards/formulas/FML-部分和=卷积（Dirichlet核）]]
- 公式（闭式）：[[Content/傅里叶分析/cards/formulas/FML-Dirichlet核闭式（sin比）]]
- 点态收敛主线（Dirichlet 定理）：[[Content/傅里叶分析/notes/第03章 Fourier级数的收敛性/3.2 逐点收敛]]

## 1. 定义（两种等价形式）
Dirichlet 核定义为指数和：
- $D_N(x)=\sum_{|n|\le N} e^{inx}$。

它也有闭式表达（见卡片真源）：
- $D_N(x)=\frac{\sin((N+\tfrac12)x)}{\sin(x/2)}$（在 $x\ne 0$ 时；$x=0$ 时用极限定义）。

## 2. 为什么它“坏”（直觉与结论）
把部分和写成卷积：
- $S_N f=f*D_N$。

这意味着 $S_N$ 是否收敛，要看核族 $\{D_N\}$ 是否像“近似恒等”。但它失败在：
1) **非负性失败**：$D_N$ 强振荡、符号变化。  
2) **$L^1$ 质量增长**：$\|D_N\|_{L^1}$ 随 $N$ 增长（典型为对数增长），因此卷积算子在 $C(\mathbb T)$ 上不可能一致有界。  
3) **“局部平均”直觉失效**：虽然 $D_N$ 的积分归一化成立，但它不是好核，不能直接保证 $f*D_N\to f$。

## 2.5 坏核体检表（可复用）
| 检查项 | 结论 | 意味着什么 |
|---|---|---|
| 归一化 | 成立 | 仅说明“常数不变”，不保证收敛 |
| 非负性 | 失败 | 强振荡与过冲不可避免 |
| $\|D_N\|_{L^1}$ | 增长（典型对数） | 卷积算子不可能在 $C(\mathbb T)$ 上一致有界 |
| 质量集中 | 不满足好核口径 | 无法直接用“好核逼近”一键推出收敛 |

## 3. 与换核求和法的对照
- Cesàro 平均把 $D_N$ 换成 Fejér 核 $F_N$（非负好核），收敛性质显著增强。  
- Abel 平均把 $D_N$ 换成 Poisson 核 $P_r$（非负好核），同理更稳。

## 4. 常见误区
- 把 $S_N f$ 当成“更精细的平滑逼近”：实际上它可能更振荡，必须配合正则性（如 BV）或改用求和法。

## 5. 参见
- $L^1$ 增长相关估计：[[Content/傅里叶分析/cards/theorems/EST-共轭Dirichlet核L1对数估计]]
- 对照的好核：[[Content/傅里叶分析/concepts/Fejer核]]、[[Content/傅里叶分析/concepts/Poisson核]]
