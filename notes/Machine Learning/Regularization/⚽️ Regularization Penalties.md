---
title: ⚽️ Regularization Penalties
layout: default
---

# ⚽️ Regularization Penalties

Regularization penalties force weights to be smaller, preventing over-reliance on certain features in the training data and therefore preventing overfitting.

Penalties commonly use [[📌 Norms]] on the weights scaled by a strength coefficient, adding $$\lambda\Vert w \Vert_p^p$$ to the loss function.
1. Ridge regression uses $$L_2$$ norm, which encourages all weights to be smaller and shrinks larger weights the most. This is equivalent to applying MAP in [💰 Linear Regression](/public-garden/notes/Machine Learning/Supervised Learning/💰 Linear Regression.html).
2. Lasso regression uses $$L_1$$ norm, which evenly shrinks all weights and drives some to $$0$$, performing feature selection. Optimization requires [⛰️ Gradient Descent](/public-garden/notes/Machine Learning/Optimization/⛰️ Gradient Descent.html).
3. With $$L_0$$ norm, we get a penalty that only cares about how many weights are $$0$$, again performing feature selection, which is optimized with [🔎 Greedy Search](/public-garden/notes/Machine Learning/Optimization/🔎 Greedy Search.html).

The following is an example of how $$L_0$$, Ridge, and Lasso shrink a hyperparameter's values. X-axis is the original value, and Y-axis is the new value.
<div style="text-align:center">
<img src="{{ site.URL }}/TEST/notes/Attachments/notes/Attachments/20221229103145.png.png" width="500"/>
</div>

Elastic-net uses both $$L_1$$ and $$L_2$$ loss, which shrinks large weights and feature selects at the same time.

The following is a visual example of the difference between Lasso, Ridge, and Elastic-net. The rings represent contours of the loss function, and colored shapes are contours of the penalty; their intersection is the optimal parameter setting.

![notes/Attachments/20221229103146.png](notes/Attachments/20221229103146.png.png)