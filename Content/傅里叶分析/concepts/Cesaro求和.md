---
title: "Cesaro求和"
type: concept
tags:
  - 傅里叶分析
  - 求和法
  - concept
date: 2026-04-24
cssclasses:
  - wide-page
status: mature
---

> [!abstract] 定位（一句话）
> Cesaro 求和（$(C,1)$）就是对 Fourier 部分和再做平均（等价于与 Fejer 核卷积），从而把“坏核”替换为“好核”并得到更稳健的收敛。
^overview

## 真源回链（先止血）
- 第02章主线：[[Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/2.5 Cesaro和Abel求和]]
- 概念：[[Content/傅里叶分析/concepts/Cesaro平均]]、[[Content/傅里叶分析/concepts/Fejer核]]
- 定理：[[Content/傅里叶分析/cards/theorems/THM-Fejér定理（Cesàro求和一致收敛）]]

## 1. 定义（一般级数口径）
设 $\sum_{n\ge 0} a_n$ 的部分和为
$$ s_N=\sum_{n=0}^{N} a_n. $$
其 Cesaro 平均定义为
$$ \sigma_N=\frac{1}{N+1}\sum_{k=0}^{N} s_k. $$
若 $\sigma_N\to S$，则称原级数在 Cesaro 意义下可求和到 $S$，记作 $\sum a_n \stackrel{C,1}{=} S$。

直觉：对部分和再平均，平滑掉振荡或过冲。

## 2. 关键性质（速查）
| 性质 | 含义 |
|---|---|
| 线性 | 对线性组合保持线性 |
| 正则性 | 若 $\sum a_n$ 通常收敛到 $S$，则 Cesaro 和也等于 $S$ |
| “平均”是核心 | 许多稳定性来自“对部分和再平均”的降噪效果 |

## 3. Fourier 场景中的落地：Cesaro 平均与 Fejér 核
Fourier 场景中更常用的是对 Fourier 部分和的 Cesaro 平均
$$ \sigma_N f(x)=\frac{1}{N+1}\sum_{k=0}^{N} S_k f(x). $$
它等价于与 Fejér 核卷积 $\sigma_N f=f*F_N$，因此可直接用好核逼近定理得到更稳健的收敛结论（Fejér 定理）。

## 4. 常见误区
- ❌ “Cesaro 求和能修复一切发散”；✅ 它只是一个具体求和法，结论依赖对象与口径（例如连续函数上一致收敛是 Fourier 特例）。  
- ❌ 混淆 “一般级数的 Cesaro 求和” 与 “Fourier 部分和的 Cesaro 平均”；✅ 后者是前者在 Fourier 部分和序列上的应用（见 [[Cesaro平均]]）。  

## 5. 参见
- 对照：[[Content/傅里叶分析/concepts/Abel求和]]、[[Content/傅里叶分析/concepts/Abel平均]]
