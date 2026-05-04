---
title: "MTH-ε细分法（压U-L到任意小）"
type: card
card_type: method
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第09章 9.1–9.2"
tags:
  - 傅里叶分析/cards
  - method
  - integration
  - riemann
---

> [!abstract]
> Riemann 体系最通用的证明模板：把目标转成“找到一个分割使 $U(P,f)-L(P,f)<\varepsilon$”。连续性提供一致连续，从而“网格足够细 ⇒ 局部振荡足够小”；再由 $U-L$ 的加权和分解完成全局估计。

# 可调用口径
- Step 1：把误差写成 $U-L=\sum \omega_S|S|$（$\omega_S$ 为子块振荡）。
- Step 2：用一致连续：选 $\delta$ 使“直径 < $\delta$ ⇒ 振荡 < \varepsilon/|R|”。
- Step 3：取分割网格 < $\delta$，从而 $U-L<\varepsilon$。

# 真源（勿在本卡重复维护）
![[9.2 多重积分#^pf-9-2-continuous-integrable]]

