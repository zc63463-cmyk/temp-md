---
title: "THM-Parseval恒等式（圆周Plancherel）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第03章"
tags:
  - 傅里叶分析/cards
  - theorem
  - L2
  - Parseval
  - Plancherel
  - 完备性
---

> [!abstract]
> 指数系在 $L^2(\mathbb T)$ 的完备性等价于能量守恒：$\|f\|_2^2=\sum|\widehat f(n)|^2$。
>
# 可调用口径
- **结论**：对 $f\in L^2(\mathbb T)$，有 $\|f\|_2^2=\sum_{n\in\mathbb Z}|\widehat f(n)|^2$（圆周 Plancherel/Parseval）。
- **适用条件**：依赖指数系在 $L^2(\mathbb T)$ 的完备性（等价于三角多项式稠密）。
- **含义**：Fourier 变换把 $L^2$ 等距地送到 $\ell^2$（能量守恒/无信息损失）。
- **常用用途**：把误差能量写成“尾部平方和”，从而得到 $\|f-S_N f\|_2\to 0$。
- **对照**：若只知道正交性但不知完备性，则只能得到 Bessel（$\le$）。
- **注意**：这是 $L^2$ 理论；点态收敛需要额外分析（3.2）。

# 真源（勿在本卡重复维护）
![[3.1 Fourier级数的均方收敛#^pf-3-1-parseval]]

# 关联
- 章节：[[第03章 Fourier级数的收敛性 — 章节汇总]]｜[[第03章 Fourier级数的收敛性 — ingest(MOC)]]
- 上游：[[THM-Bessel不等式（L2）]]
- 下游：[[THM-Fourier部分和的L2均方收敛（S_N f→f）]]
