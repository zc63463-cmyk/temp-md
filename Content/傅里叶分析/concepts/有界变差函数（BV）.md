---
title: "有界变差函数（BV）"
type: concept
tags:
  - 傅里叶分析
  - BV
  - concept
date: 2026-04-24
cssclasses:
  - wide-page
status: mature
---

> [!abstract] 定位（一句话）
> BV（有界变差）是一种足以控制振荡积分的局部正则性；它是 Dirichlet 点态收敛定理中的典型可用假设。
^overview

## 真源回链（先止血）
- 对象卡片：[[Content/傅里叶分析/cards/objects/OBJ-有界变差（BV）在Dirichlet收敛中的角色]]
- Dirichlet 点态收敛定理：[[Content/傅里叶分析/cards/theorems/THM-Dirichlet点态收敛定理（BV_分段光滑）]]
- 章节真源：[[Content/傅里叶分析/notes/第03章 Fourier级数的收敛性/3.2 逐点收敛]]

## 1. 定义（工作口径）
设 $f:[a,b]\to\mathbb R$。定义其变差
$$ V_a^b(f)=\sup_{\Pi}\sum_{j}|f(x_j)-f(x_{j-1})|, $$
上确界对所有分割 $\Pi: a=x_0<x_1<\cdots<x_n=b$ 取。若 $V_a^b(f)<\infty$，称 $f$ 在 $[a,b]$ 上有界变差（$f\in BV([a,b])$）。

## 2. 关键性质（与 Fourier 点态收敛相关）
| 性质 | 在本书中的用途 |
|---|---|
| 左右极限存在 | BV 函数在每点都有左右极限（至多可去可数跳点），适配“跳点取平均”的极限口径 |
| 可控振荡积分 | BV 允许对振荡积分做分部积分/Dirichlet 判别型估计，是 Dirichlet 定理证明链的技术核心 |
| 分段光滑 ⊂ BV | 分段 $C^1$（或分段单调）通常自动满足 BV，因此 BV 是更一般的可用假设 |

## 3. 在 Dirichlet 点态收敛中的角色（最短解释）
Dirichlet 部分和可写为
$$ S_N f(x)=\frac{1}{2\pi}\int_{-\pi}^{\pi} f(x-y)\,D_N(y)\,dy. $$
由于 $D_N$ 强振荡，证明点态收敛要把积分改写为“振荡项 + BV 可控项”的形式；BV 提供了把振荡项压到可控误差的通道，最终得到
$$ S_N f(x)\to \frac{f(x+)+f(x-)}{2}. $$

## 4. 常见误区
- ❌ 以为“BV = 可导”；✅ BV 允许跳跃不连续，但总振荡量有限。  
- ❌ 以为“BV 自动保证部分和处处收敛到 $f(x)$”；✅ 跳点处的正确口径是左右平均而非点值本身。  
