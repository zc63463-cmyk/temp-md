---
title: "Cesaro平均"
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
> Cesaro 平均（$(C,1)$）用部分和的平均替代原部分和，相当于与 Fejer 核卷积；因此比 Dirichlet 部分和更稳定，并给出 Fejér 定理的一致收敛结论。
^overview

## 真源回链（先止血）
- 定理入口：[[Content/傅里叶分析/cards/theorems/THM-Fejér定理（Cesàro求和一致收敛）]]
- Fejer 核口径：[[Content/傅里叶分析/concepts/Fejer核]]
- 第02章求和法主线：[[Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/2.5 Cesaro和Abel求和]]

## 1. 定义（平均部分和）
设 $S_N f$ 为 Fourier 部分和，则 Cesaro 平均（$(C,1)$）定义为
$$ \sigma_N f(x)=\frac{1}{N+1}\sum_{k=0}^{N} S_k f(x). $$

直觉：对部分和再做平均，降低 Dirichlet 部分和的振荡与过冲。

## 2. 与卷积/乘子等价
由 $S_k f=f*D_k$（卷积表示），得到
$$ \sigma_N f=f*F_N, $$
其中 $F_N$ 是 Fejer 核（见 [[Fejer核]]）。

频域视角下，$\sigma_N$ 的乘子是“三角形窗口”：
- $|n|\le N$ 时，权重为 $1-\frac{|n|}{N+1}$；
- $|n|>N$ 时，权重为 $0$。

## 3. 收敛口径（Fejér 定理）
Cesaro 平均的稳定性来自 $F_N$ 是好核（非负、归一化、质量集中），因此：
- 若 $f\in C(\mathbb T)$，则 $\sigma_N f\to f$ 一致收敛；  
- 若 $f\in L^1(\mathbb T)$，则在 Lebesgue 点处 $\sigma_N f(x)\to f(x)$；  
- 若 $f(x\pm)$ 存在，则
$$ \sigma_N f(x)\to \frac{f(x+)+f(x-)}{2}. $$

## 4. 与 Dirichlet 部分和对照（坏核→好核）
| 维度 | Cesaro 平均 $\sigma_N$ | 部分和 $S_N$ |
|---|---|---|
| 核 | Fejer 核 $F_N$（好核，非负） | Dirichlet 核 $D_N$（坏核，振荡） |
| $L^1$ 控制 | 归一化后恒为 1 | $\|D_N\|_{L^1}$ 增长 |
| 频域窗口 | 三角形窗口（软化） | 硬截断 |

## 5. 常见误区
- ❌ “Cesaro 平均能修复任何发散”；
  ✅ 它是一个具体算子，保证收敛的口径是“连续函数一致收敛、可积函数在 Lebesgue 点处收敛”。  
- ❌ 混淆“序列的 Cesaro 平均”与“Fourier 部分和的 Cesaro 平均”；
  ✅ 对象不同，但机制相同：都是对部分和再平均。

## 6. 参见
- Fejer 核：[[Fejer核]]
- 对照：[[Dirichlet核]]、[[Abel平均]]
- 一般级数口径：[[Cesaro求和]]
