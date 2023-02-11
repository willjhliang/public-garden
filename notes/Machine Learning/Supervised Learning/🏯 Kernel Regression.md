---
title: 🏯 Kernel Regression
layout: default
parent: 🤖 Machine Learning
---

# 🏯 Kernel Regression

## Theory
Kernel Regression is similar to [🏠 K-Nearest Neighbors](/public-garden/notes/Machine Learning/Supervised Learning/🏠 K-Nearest Neighbors.html). However, instead of a hard $$K$$ cutoff, we get the average across all data points weighted by their similarity as measured by [🍿 Kernels](/public-garden/notes/Mathematics/🍿 Kernels.html).

## Prediction
Given input $$x$$ and training data $$D$$,
1. For regression, return 

$$

\hat{y} = \frac{\sum_{i=1}^n k(x, x_i)y_i}{\sum_{i=1}^n k(x, x_i)}

$$

2. For classification, return 

$$

\hat{y} = sign(\sum_{i=1}^n k(x, x_i) y_i)

$$

