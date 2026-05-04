---
title: "THM-Fourier系数唯一性（Poisson核_Abel平均）"
aliases:
  - "THM-Fourier系数唯一性（通过Poisson核/Abel平均）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第02章"
tags:
  - 傅里叶分析/cards
  - theorem
  - 唯一性
  - Poisson核
  - Abel求和
---

> [!abstract]
> 这一定理的机制是“先平滑再取极限”：用 Abel 平均（Poisson 核）把 Fourier 数据变成绝对收敛的卷积 $f*P_r$，从而可稳定地读出“若系数全为 0，则所有平滑版本都为 0”；再用好核逼近让平滑版本在 $r\uparrow 1$ 时恢复原函数（a.e.），得到唯一性。
>
>
# 1. 结论（可调用口径）
若 $f\in L^1(\mathbb T)$ 且对所有 $n\in\mathbb Z$ 有 $\widehat f(n)=0$，则 $f=0$（几乎处处）。

# 2. 条件作用
- $L^1$：确保 Fourier 系数定义与卷积 $f*P_r$ 有意义，并可使用 Lebesgue 点/逼近恒等框架。  
- “对所有 $n$ 系数为 0”：这是“数据为零”的假设；结论只能到 a.e.（零测集不可辨识）。

# 3. 证明骨架（只留主干）
- Step 1：定义 Abel 平均 $A_r f(x)=\sum_{n\in\mathbb Z} r^{|n|}\widehat f(n)e^{inx}$（$0<r<1$），并识别 $A_r f=f*P_r$。  
- Step 2：用卷积-乘法结构：$\widehat{A_r f}(n)=r^{|n|}\widehat f(n)=0$，因此对每个 $r$ 有 $A_r f\equiv 0$。  
- Step 3：$P_r$ 形成好核（$r\uparrow 1$），在 Lebesgue 点处 $(f*P_r)(x)\to f(x)$。  
- 关键一跳：**用“好核极限”把 $A_r f\equiv 0$ 推回 $f\equiv 0$（a.e.）**。

> [!faq]- 完备证明（真源）
> 见：[[2.2 Fourier级数的唯一性#^pf-2-2-uniqueness-via-poisson]]
>
# 4. 最容易“看懂但不会用”的点
1) 把唯一性误解为 $S_N f\to f$：唯一性是“数据可恢复”，不要求部分和点态收敛。  
2) 忽略 $0<r<1$ 的门票作用：绝对收敛保证交换求和/积分与卷积识别。  
3) 没有意识到“a.e.”是自然极限：在 $L^1$ 框架下，点值恢复必须经过 Lebesgue 点。  
4) 误把“Poisson 核是好核”当作直觉：严格证明依赖归一化 + 非负 + 质量集中。

# 5. 关联
- 来源小节：[[2.2 Fourier级数的唯一性]]  
- 上游：[[FML-卷积使 Fourier 系数相乘]]、[[OBJ-好核（近似恒等）]]  
- 并行：[[THM-Fejér定理（Cesàro求和一致收敛）]]（同属“换核修正求和”）  
