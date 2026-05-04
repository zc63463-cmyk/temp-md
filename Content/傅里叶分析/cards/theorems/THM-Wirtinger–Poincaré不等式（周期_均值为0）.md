---
title: "THM-Wirtinger–Poincaré不等式（周期_均值为0）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第03章 3.3"
tags:
  - 傅里叶分析/cards
  - theorem
  - Poincare不等式
  - Wirtinger
  - Parseval
---

> [!abstract]
> 周期函数在“均值为 0”约束下，可用导数控制本身：这是 Fourier/Parseval 的一条典型应用（频域权重 $n^2$）。
>
>
# 可调用口径
- **结论**（典型口径）：若 $f$ 为 $2\pi$-周期且 $\widehat f(0)=0$，则 $\|f\|_2 \le \|f'\|_2$（常数随归一化约定而定）。
- **频域解释**：$\widehat{f'}(n)=in\widehat f(n)$，于是 $\sum |\widehat f(n)|^2 \le \sum n^2|\widehat f(n)|^2$（去掉 $n=0$）。
- **常用用途**：把“函数大小”转成“能量在高频的加权大小”，用于稳定性/唯一性/估计。
- **注意**：必须去掉常数项（均值为 0）；否则导数无法控制常数模式。
- **对照**：这是 Poincaré 不等式在圆周上的 Fourier 版本；在区间/高维也有对应形式。

# 真源（勿在本卡重复维护）
![[3.3 练习#^pf-3-3-11]]

# 关联
- [[FML-Fourier系数与部分和（定义）]]
- [[THM-Parseval恒等式（圆周Plancherel）]]

