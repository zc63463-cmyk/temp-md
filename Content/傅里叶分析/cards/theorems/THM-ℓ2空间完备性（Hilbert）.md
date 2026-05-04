---
title: "THM-ℓ2空间完备性（Hilbert）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第03章 3.3"
tags:
  - 傅里叶分析/cards
  - theorem
  - Hilbert空间
  - ell2
  - 完备性
---

> [!abstract]
> $\ell^2(\mathbb Z)$ 是 Hilbert 空间：每个 Cauchy 列在 $\ell^2$ 范数下收敛到某个 $\ell^2$ 元素。
>
>
# 可调用口径
- **结论**：任意 $\ell^2$-Cauchy 列都存在极限 $x\in\ell^2$，且 $\|x^{(k)}-x\|_{\ell^2}\to 0$。
- **证明模板**：逐坐标收敛 + Fatou（或下极限不等式）保证极限仍在 $\ell^2$ + 再用范数 Cauchy 推出范数收敛。
- **常用用途**：把“系数平方可和”作为稳定空间来做极限交换、逼近与投影论证。
- **对照**：$\ell^1$ 不完备（在更精细的范数/空间里会出问题），$\ell^2$ 的完备性是 $L^2$ 理论顺利运转的底层原因之一。
- **注意**：不要把“逐点极限存在”误当成“范数极限存在”，必须显式使用 Fatou/一致控制。

# 真源（勿在本卡重复维护）
![[3.3 练习#^pf-3-3-02]]

# 关联
- 章节入口：[[第03章 Fourier级数的收敛性 — ingest(MOC)]]
- 上游：[[THM-Parseval恒等式（圆周Plancherel）]]

