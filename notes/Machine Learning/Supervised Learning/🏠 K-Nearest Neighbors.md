---
title: 🏠 K-Nearest Neighbors
layout: default
---

# 🏠 K-Nearest Neighbors

# Theory
K-Nearest Neighbors assumes that similar $$x$$ will have similar $$y$$; in other words, the label of any unknown $$x$$ can be estimated by checking the labels of similar $$x$$ that we _do_ know.

Specifically, we’ll check the $$K$$ most similar data points, calculated by some distance function $$d$$, and get an aggregate of their labels $$y$$. The distance is commonly one of the [📌 Norms](/public-garden/notes/Mathematics/📌 Norms.html), usually $$L_1$$ or $$L_2$$.

The following visually demonstrates the effect of different norms for the distance function, using $$L_2$$, $$L_1$$, and $$L_{\inf}$$ respectively (with $$K = 1$$).

<div style="text-align:center">
<img src="{{ site.url }}{{ site.baseurl }}/notes/Attachments/20221229103203.png?raw=true"/>
</div>

$$K$$ also affects our decision boundary, with higher $$K$$ giving a smoother separation. Below is a comparison between $$K=1$$ and $$K = 3$$.

<div style="text-align:center">
<img src="{{ site.url }}{{ site.baseurl }}/notes/Attachments/20221229103204.png?raw=true" width="420"/>
</div>


## Prediction
Given input $$x$$, training data $$D$$, and distance function $$d$$. Find $$\{j_1, \dots, j_k\}$$ closest examples in $$D$$ to $$x$$ with respect to $$d$$.

For regression, return the average 

$$

\frac{1}{K} \sum_{k=1}^K y_{j_k}

$$

For classification, return the majority 

$$

sign(\sum_{k=1}^K y_{j_k})

$$

