---
title: "Fejer核"
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
> Fejer 核 $F_N$ 是 Cesaro 平均（$(C,1)$）的卷积核：它是非负的好核，因此给出连续函数的 Cesaro 求和一致收敛（Fejér 定理）。
^overview

## 真源回链（先止血）
- 定理入口：[[Content/傅里叶分析/cards/theorems/THM-Fejér定理（Cesàro求和一致收敛）]]
- 第02章求和法主线：[[Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/2.5 Cesaro和Abel求和]]
- 练习真源（Fejér 核闭式）：[[Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/2.6 练习]]

## 1. 定义
Fejer 核 $F_N$ 是 Dirichlet 核的平均（因此对应 Cesaro 平均）。

- 平均定义：
$$ F_N(x)=\frac{1}{N+1}\sum_{k=0}^{N}D_k(x). $$

- 平方闭式（直接给出非负性）：
$$ F_N(x)=\frac{1}{N+1}\left(\frac{\sin\big((N+1)x/2\big)}{\sin(x/2)}\right)^2. $$

## 2. 关键性质（速查）
| 性质 | 结论 | 备注 |
|---|---|---|
| 非负性 | $F_N(x)\ge 0$ | 由平方闭式 |
| 归一化（质量为 1） | $$ \frac{1}{2\pi}\int_{-\pi}^{\pi}F_N(x)\,dx=1 $$ | 等价于 $\widehat{F_N}(0)=1$ |
| 频域窗口 | $\widehat{F_N}(n)=1-\frac{|n|}{N+1}$（当 $|n|\le N$），且 $\widehat{F_N}(n)=0$（当 $|n|>N$） | “三角形窗口” |
| 好核 | $N\to\infty$ 时质量向 $0$ 集中 | 见 [[好核（逼近恒等）]] |

## 3. 与卷积/乘子等价
Cesaro 平均（函数级数口径）定义为
$$ \sigma_N f(x)=\frac{1}{N+1}\sum_{k=0}^{N}S_k f(x). $$
由 $S_k f=f*D_k$ 得到
$$ \sigma_N f=f*F_N. $$
因此 $F_N$ 对应的频域权重正是上面的“三角形窗口”，它把硬截断软化为线性衰减。

## 4. 收敛口径（Fejér 定理的算子版）
- 连续函数口径：若 $f\in C(\mathbb T)$，则 $\sigma_N f\to f$ 一致收敛。  
- $L^1$ 口径：若 $f\in L^1(\mathbb T)$，则在 Lebesgue 点处 $\sigma_N f(x)\to f(x)$。  
- 跳点口径：若 $f(x\pm)$ 存在，则（偶核/对称化机制）
$$ \sigma_N f(x)\to \frac{f(x+)+f(x-)}{2}. $$

## 5. 与 Dirichlet 核对照（为什么平均能修复振荡）
| 维度 | Fejer 核 $F_N$（Cesaro） | Dirichlet 核 $D_N$（部分和） |
|---|---|---|
| 空间域 | 非负、像局部平均 | 强振荡、变号 |
| $L^1$ | 归一化后恒为 1 | $\|D_N\|_{L^1}$ 随 $N$ 增长 |
| 频域窗口 | 三角形窗口（线性衰减） | 硬截断 |

## 6. 常见误区
- ❌ 把 $F_N$ 当成 $D_N$；✅ $F_N$ 是对 $D_k$ 的平均，平方闭式保证了正性。  
- ❌ 把分母写成 $N$；✅ 本库口径统一使用 $N+1$（与 §2.5 保持一致）。  

## 7. 参见
- Cesaro 平均：[[Cesaro平均]]
- 对照：[[Dirichlet核]]、[[Poisson核]]
