---
title: "Wiener测度"
type: concept
chapter: "第06章"
tags:
  - 泛函分析
  - 概率论
  - Wiener测度
  - Brownian运动
aliases:
  - "Wiener measure"
sources:
  - "张恭庆《泛函分析讲义》第06章"
  - "Wikipedia: Wiener measure"
date: 2026-04-21
related:
  - "[[Brownian运动]]"
  - "[[Kolmogorov扩张定理]]"
  - "[[Kolmogorov连续性定理]]"
---

# Wiener测度

> [!abstract] 概述
> ==Wiener 测度==是定义在路径空间（典型为 $C([0,T])$ 或 $C([0,\infty))$）上的概率测度，使得“坐标过程”成为 Brownian 运动。  
> 它把“随机过程”落实为一个真正的测度对象：构造（6.3）就是在构建这件事。

## 定义

> [!def] Wiener 测度（提示性）
> 在 $C([0,T])$ 上存在概率测度 $\mathbb W$，使得坐标映射 $X_t(\omega)=\omega(t)$ 满足 Brownian 的有限维分布，并且路径连续性由空间本身保证。

## 核心性质（命题工具箱）

| 性质/命题 | 表述 | 用途 |
|---|---|---|
| 构造来源 | 一致有限维分布 + Kolmogorov 扩张 | 把网格分布拼成路径测度 |
| 连续性保证 | 通过连续性定理得到连续版本 | 解释“为何路径连续” |
| 坐标过程 | $X_t(\omega)=\omega(t)$ | 在路径空间上定义过程 |

## 关系网络

```mermaid
graph TB
  A["有限维分布一致性"] --> B["Kolmogorov扩张定理"]
  B --> C["Wiener测度"]
  C --> D["坐标过程"]
  D --> E["Brownian运动"]

  style C fill:#5cb85c,color:#fff
  style E fill:#e8a838,color:#fff
```

## 章节扩展

### 第06章：Brownian运动引论

- 构造主线：[[6.3 Brownian运动的构造#二、核心思想]]
- 技巧准备：[[6.2 技巧准备#二、核心思想]]

## 补充

> [!info] 参考（权威外链）
> - https://en.wikipedia.org/wiki/Wiener_measure

## 参见

- [[Brownian运动]]
- [[Kolmogorov扩张定理]]
- [[Kolmogorov连续性定理]]

