---
title: "FML-部分和=卷积（Dirichlet核）"
type: card
card_type: formula
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第02章"
tags:
  - 傅里叶分析/cards
  - formula
  - Dirichlet核
  - 部分和
  - 核方法
---

> [!abstract]
> 这是把“Fourier 级数收敛”转写为“核族性质”的关键接口：部分和算子 $S_N$ 不是逐点求和，而是一个卷积算子（频域硬截断的空间表现）。
>
>
# 1. 公式
令 Dirichlet 核 $D_N(x)=\sum_{|n|\le N}e^{inx}$，则对 $f\in L^1(\mathbb T)$：
$$ S_N f = f*D_N. $$

# 2. 角色
- 桥梁恒等式：把“求和过程”变成“对 $f$ 施加滤波器 $D_N$”。  
- 一旦写成卷积，收敛/估计问题就被移交给核分析（$L^1$、振荡、质量集中等）。

# 3. 它连接了哪两步
1) 频域：$S_N$ 对 $\widehat f(n)$ 做硬截断（$|n|\le N$ 保留，否则丢弃）。  
2) 空间：硬截断对应一个强振荡核 $D_N$，从而收敛可能失败（这不是“系数不好”，而是“核不好”）。

# 4. 为什么值得单独保存
- 它是第02章后半（好核与可求和）的一切动机来源：  
  - Dirichlet 核不是好核 ⇒ 点态收敛微妙；  
  - Cesàro/Abel 的本质是把坏核换成好核（Fejér/Poisson）。

# 5. 推导骨架
- 先计算 $\widehat{D_N}(k)$：它等于 1（$|k|\le N$）否则 0；  
- 用卷积-乘法公式：$\widehat{f*D_N}(k)=\widehat f(k)\widehat{D_N}(k)$；  
- 得到 $f*D_N$ 与 $S_N f$ 具有相同 Fourier 系数，因此相同。

> [!faq]- 完备证明（真源）
> 见：[[2.3 卷积#^pf-2-3-sn-conv-dn]]
>
# 6. 最容易误用的点
1) 把 $S_N$ 误当“平均”：$D_N$ 非正且 $L^1$ 可能增长，完全不同于局部平均。  
2) 忽略周期性：这是圆周卷积口径，区间/实线需要相应改写。  
3) 看到 $D_N(0)=2N+1$ 就以为“越大越好”：真正的风险在远处振荡尾巴与 $L^1$ 控制。

# 7. 关联
- 上游：[[FML-卷积使 Fourier 系数相乘]]  
- 下游：[[OBJ-好核（近似恒等）]]、[[THM-Fejér定理（Cesàro求和一致收敛）]]

