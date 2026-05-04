---
title: "Lebesgue点"
type: concept
tags:
  - 傅里叶分析
  - measure
  - concept
date: 2026-04-24
cssclasses:
  - wide-page
status: mature
---

> [!abstract] 定位（一句话）
> Lebesgue 点是“局部平均逼近点值”的典型点；好核卷积的点态收敛结论通常在 Lebesgue 点成立。
^overview

## 真源回链（先止血）
- 第02章好核的点态口径：[[Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/2.4 好核]]
- 好核逼近定理：[[Content/傅里叶分析/cards/theorems/THM-好核逼近定理]]

## 1. 定义（工作口径）
设 $f\in L^1_{\mathrm{loc}}(\mathbb T)$。点 $x$ 称为 $f$ 的 Lebesgue 点，若
$$ \lim_{r\downarrow 0}\frac{1}{2r}\int_{x-r}^{x+r}|f(y)-f(x)|\,dy=0. $$

直觉：在 Lebesgue 点处，“以 $x$ 为中心的小区间平均”能够恢复 $f(x)$，且误差在尺度趋于 0 时消失。

## 2. 关键性质（为什么它重要）
| 性质 | 含义 |
|---|---|
| 几乎处处成立 | 若 $f\in L^1(\mathbb T)$，则 Lebesgue 点在测度意义下“几乎处处”存在 |
| 连接到卷积逼近 | 若 $K_\alpha$ 是好核，则在 Lebesgue 点 $x$ 处有 $(f*K_\alpha)(x)\to f(x)$ |
| 连续点是特例 | 若 $f$ 在 $x$ 连续，则 $x$ 必是 Lebesgue 点 |

## 3. 与好核逼近的接口（最常用的推理模板）
在证明 $(f*K_\alpha)(x)\to f(x)$ 时，经常把误差写成
$$ (f*K_\alpha)(x)-f(x)=\frac{1}{2\pi}\int_{-\pi}^{\pi}(f(x-y)-f(x))K_\alpha(y)\,dy, $$
然后分成“近区 + 远区”：
- 近区：Lebesgue 点定义控制 $f(x-y)-f(x)$ 的局部平均误差；
- 远区：好核的质量集中控制 $\int_{|y|>\delta}|K_\alpha(y)|$。

对应概念页：[[Content/傅里叶分析/concepts/分裂积分区域估计]]、[[Content/傅里叶分析/concepts/局部性质×核集中]]。

## 4. 常见误区
- ❌ 把 “Lebesgue 点”当作“处处连续”的替代；✅ 它是几乎处处的“平均意义下的好点”，不保证处处。  
- ❌ 忽略“点态结论的口径”；✅ 对 $L^1$ 函数，最自然的点态口径通常是 Lebesgue 点而不是任意点。  
