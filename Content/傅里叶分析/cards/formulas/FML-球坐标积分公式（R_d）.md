---
title: "FML-球坐标积分公式（R_d）"
type: card
card_type: formula
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第09章 9.2"
tags:
  - 傅里叶分析/cards
  - formula
  - integration
  - polar
---

> [!abstract]
> 在 $R^d$ 上把积分拆成“径向 × 角向”的标准公式：Jacobian 给出 $r^{d-1}$，这是 Fourier 分析（径向核/Bessel 接口/体积估计）最常用的计算入口。

# 可调用口径
- 对适当可积 $F$：
  $$\int_{\mathbb R^d}F(x)\,dx=\int_{S^{d-1}}\int_0^\infty F(r\omega)\,r^{d-1}\,dr\,d\omega.$$

# 真源（勿在本卡重复维护）
![[9.2 多重积分#^thm-9-2-polar]]
![[9.2 多重积分#^pf-9-2-polar]]

