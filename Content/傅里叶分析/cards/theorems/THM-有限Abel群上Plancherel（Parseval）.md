---
title: "THM-有限Abel群上Plancherel（Parseval）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第07章 7.2"
tags:
  - 傅里叶分析/cards
  - theorem
  - finite-fourier
  - abelian-group
  - Plancherel
  - Parseval
---

> [!abstract]
> 有限 Abel 群上的能量恒等式：把 $L^2(G)$ 的内积转换到对偶群 $\widehat G$ 上（差一个固定比例）。

# 可调用口径
- 将 $\sum_{x\in G}|f(x)|^2$ 转换为 $(1/|G|)\sum_{\chi\in\widehat G}|\widehat f(\chi)|^2$，便于估计。
- 常见搭配：Fourier trick（点乘/能量 + Cauchy–Schwarz）。
- 归一化敏感：是否有 $1/|G|$ 完全由定义决定；本卡按节笔记约定。

# 真源（勿在本卡重复维护）
![[7.2 有限Abel群上的Fourier分析#^thm-7-2-plancherel]]
![[7.2 有限Abel群上的Fourier分析#^pf-7-2-plancherel]]

