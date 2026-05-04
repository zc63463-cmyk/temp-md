---
title: "THM-Weierstrass处处不可微（疏频）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第04章 4.3"
tags:
  - 傅里叶分析/cards
  - theorem
  - 处处不可微
  - Weierstrass函数
  - lacunary
---

> [!abstract]
> Weierstrass 型疏频三角级数给出“连续但处处不可微”的经典例子：连续性靠一致收敛，不可微性靠尺度选择让某一高频项主导差商。
>
>
# 可调用口径
- **结论**：在书中给定参数条件下，$W(x)=\sum_{n\ge 0}a^n\cos(b^n x)$ 连续但处处不可微。
- **连续性**：由 $0<a<1$，$\sum a^n$ 收敛，故一致收敛 ⇒ 连续。
- **不可微性模板**：选 $h_m\approx b^{-m}$，让第 $m$ 项差商贡献约为 $a^m b^m$；其余项按 $n<m$（Lipschitz）与 $n>m$（粗界）拆分成可控误差。
- **参数条件角色**：确保主项严格压过误差项，从而差商在每点都不收敛。
- **注意**：系数衰减不等于“更光滑”；光滑性由高频结构决定。

# 真源（勿在本卡重复维护）
![[4.3 处处不可微的连续函数#^thm-4-3-weierstrass]]
![[4.3 处处不可微的连续函数#^pf-4-3-weierstrass]]

# 关联
- [[MTH-尺度选择法（lacunary主频支配）]]

