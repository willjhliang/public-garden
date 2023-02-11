---
title: "🍝 Independent Component Analysis"
---
# Theory
ICA is an alternative to [[🗜️ Principle Component Analysis]] where we find $S$ and $W$ such that embeddings or scores $s_j$, analogous to $z_j$ from PCA, are as independent as possible, with maximum [[|p(s_1)p(s_2)\ldots p(s_k))$$

This loss function is not quadratic, so optimization cannot be done with [[📎 Singular Value Decomposition]]. The optimization method was not covered in class.

# Prediction
Similar to PCA, we project $x^{(i)}$ onto components to get the scores of our embedding, and apply them to our components to recreate $x^{(i)}$.