---
title: "FML-L2内积（圆周归一化）"
type: card
card_type: formula
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第03章"
tags:
  - 傅里叶分析/cards
  - formula
  - L2
  - 内积
  - 归一化
---

> [!abstract]
> 圆周 $L^2(\mathbb T)$ 的常用归一化：把 $2\pi$ 的系数放进内积/系数定义，避免 Parseval 等式整体漂移。
>
# 可调用口径
- **定义**：$\langle f,g\rangle=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(x)\overline{g(x)}\,dx$。
- **适用场景**：本库的 Fourier 系数、Parseval、$S_N$ 投影等均按此归一化口径书写。
- **含义**：把周期长度的常数吸收到内积中，使指数系 $\{e^{inx}\}$ 具有标准正交关系。
- **常用用途**：保证 Parseval/Plancherel 写成“无额外常数”的等距形式。
- **注意**：若改用别的约定（如不除 $2\pi$），所有相关公式会整体多一个常数因子。
- **对照**：在第02章核语言（卷积）中，也需要保持同一归一化常数。

# 真源（勿在本卡重复维护）
![[3.1 Fourier级数的均方收敛#^fml-3-1-inner-product]]

# 关联
- [[THM-Bessel不等式（L2）]]｜[[THM-Parseval恒等式（圆周Plancherel）]]
