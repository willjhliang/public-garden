---
title: "📌 Norms"
---
Norm of $x$, denoted $||x||$, represents the “size” of the vector with three properties.
1.  $||x|| > 0$ for $x \neq 0$ and $||x|| = 0$ for $x = 0$
2.  $||kx|| = |k| * ||x||$
3.  $||x + y|| \leq ||x|| + ||y||$

$||x-y||$ is usually used as a distance measurement since it’s symmetric, non-negative, and preserves the triangle inequality.

$P$-norm is defined as $$||x||_p = (\sum_{i=1}^m |x_i|^p)^{1/p}$$
However, for extreme values of $p$, there are special norms.
1. For $p = 0$, $||x||_0 = \sum_{i=1}^m \mathbf{1}(x_i \neq 0)$. In other words, this is the number of non-zero elements in $x$.
2. For $p = \inf$, $||x||_{\inf} = \max_i |x_i|$. This is the maximum magnitude value in $x$.

>Note that $L_0$ is a pseudo-norm since it violates the second property defined above. $L_0(av) \neq |a|L_0(v)$, and instead, $L_0(av) = L_0(v)$ for $a \neq 0$.

For a matrix, we commonly use the Frobenius norm, a function of the elements in the matrix or the singular values of the matrix. $$||A||_F = \sqrt{\sum_{i=1}^n\sum_{j=1}^m|a_{i,j}|^2} = \sqrt{\sum_{i=1}^{\min(n, m)}\sigma_i^2}$$