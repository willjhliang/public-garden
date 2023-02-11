---
title: 🤖 Machine Learning
layout: default
---

# 🤖 Machine Learning

Machine learning involves algorithms that "learn" from data. The field is split into three main forms of learning depending the problem we want to solve.
1. Supervised learning deals with modeling inputs \(x\) to output \(y\).
2. Unsupervised learning finds patterns in unlabeled inputs \(x\).
3. Reinforcement learning trains a policy that maximizes an agent's long-term reward in an environment.

All three problems share a general solution structure: model formulation and optimization.

Models are represented probability distributions. They can be either generative or discriminative.
1. Generative models \(p(x, y) = p(x \vert y)p(y)\) explain how data was created.
2. Discriminative models \(p(y \vert x)\) draw boundaries in the data space.

Training these models involve optimizing their parameters, or weights.
1. [⛰️ Gradient Descent](/public-garden/notes/Machine Learning/Optimization/⛰️ Gradient Descent.html) gradually moves down a convex loss function.
2. [🔎 Greedy Search](/public-garden/notes/Machine Learning/Optimization/🔎 Greedy Search.html) performs feature selection for non-convex loss.
3. [🎉 Expectation Maximization](/public-garden/notes/Machine Learning/Optimization/🎉 Expectation Maximization.html) optimizes hidden variables in unsupervised models.

In practice, [👕 Overfitting](/public-garden/notes/Machine Learning/Regularization/👕 Overfitting.html) is a common problem where models learn noise in the training data that's not part of the real world. The solution is two-fold.
1. [⚽️ Regularization Penalties](/public-garden/notes/Machine Learning/Regularization/⚽️ Regularization Penalties.html) in loss functions apply weight shrinkage or selection.
2. [✅ Validation](/public-garden/notes/Machine Learning/Regularization/✅ Validation.html) methods find hyperparameters that optimize model complexity.

[👀 AutoML](/public-garden/notes/Machine Learning/Implementation/👀 AutoML.html) is a modern solution that automates both processes by automatically building a ensemble that maximizes performance for a given problem.

Finally, there are some more real-world practices to keep in mind.
1. [❓ Imputation](/public-garden/notes/Machine Learning/Implementation/❓ Imputation.html) is required to address missing data.
2. [💯 Evaluation](/public-garden/notes/Machine Learning/Implementation/💯 Evaluation.html) is necessary to measure a model's performance.
3. [🎙️ Interpretation and Explainability](/public-garden/notes/Machine Learning/Implementation/🎙️ Interpretation and Explainability.html) analyses the patterns our model learned and what the model actually tells us about the world.

## Supervised Learning
Supervised learning deals with learning models that act as a function mapping \(x\) to \(y\).

Non-parametric models don't optimize any weights.
1. [🏠 K-Nearest Neighbors](/public-garden/notes/Machine Learning/Supervised Learning/🏠 K-Nearest Neighbors.html) compares an input with the known data.
2. [💭 Decision Tree](/public-garden/notes/Machine Learning/Supervised Learning/💭 Decision Tree.html)s split up the data on features that give the most information about the label.
3. [🏯 Kernel Regression](/public-garden/notes/Machine Learning/Supervised Learning/🏯 Kernel Regression.html) is a soft form of KNN that considers example similarity.

An [🎻 Ensemble](/public-garden/notes/Machine Learning/Supervised Learning/🎻 Ensemble.html) combines non-parametric models to generate more accurate predictions.

Parametric models, on the other hand, have a set of weights to optimize. Many optimize the their probability likelihood using [🪙 MLE and MAP](/public-garden/notes/Machine Learning/Supervised Learning/🪙 MLE and MAP.html), while others use more model-specific methods.

While there's a huge diversity of solutions, parametric models can be categorized into the type of problem they solve: regression or classification.

Regression problems deal with predicting continuous \(y\).
1. [💰 Linear Regression](/public-garden/notes/Machine Learning/Supervised Learning/💰 Linear Regression.html) fits a line to linear data.
2. [🥢 Generalized Linear Model](/public-garden/notes/Machine Learning/Supervised Learning/🥢 Generalized Linear Model.html) adapts this idea to work for non-linear data.
3. [🔨 Principle Component Regression](/public-garden/notes/Machine Learning/Supervised Learning/🔨 Principle Component Regression.html) combines dimensionality reduction with linear regression.

Classification problems, on the other hand, work with discrete \(y\), or classes.
1. [🦠 Logistic Regression](/public-garden/notes/Machine Learning/Supervised Learning/🦠 Logistic Regression.html) is an extension of linear regression that outputs class probabilities.
2. [🛩️ Support Vector Machine](/public-garden/notes/Machine Learning/Supervised Learning/🛩️ Support Vector Machine.html)s divide the data into two classes with a hyperplane.
3. [👶 Naive Bayes](/public-garden/notes/Machine Learning/Supervised Learning/👶 Naive Bayes.html) classifies extremely large features sets by assuming that features are conditionally independent given the label.

There are some online variants of these algorithms that train via streaming, going through each datapoint one-by-one and updating the weights.
1. [🗼 Least Mean Squares](/public-garden/notes/Machine Learning/Supervised Learning/🗼 Least Mean Squares.html) is an online version of linear regression.
2. [👓 Perceptron](/public-garden/notes/Machine Learning/Supervised Learning/👓 Perceptron.html)s perform online updates for SVMs.

If there's not enough labeled data, [✋ Active Learning](/public-garden/notes/Machine Learning/Supervised Learning/✋ Active Learning.html) strategies identify the most useful datapoints to label next.

Regression and classification can also be solved with [[🧠 Deep Learning]], a subfield that uses complex neural networks to model functions.

## Unsupervised Learning
Unsupervised learning aims to capture patterns in input data \(x\). In doing so, the algorithms find a low-dimensional projection of \(x\), which captures most of the information but with less complexity.

In dimensionality reduction, we encode \(x\) into an embedding.
1. [🗜️ Principle Component Analysis](/public-garden/notes/Machine Learning/Unsupervised Learning/🗜️ Principle Component Analysis.html) is finds that embeddings that minimize distortion; in other words, these embeddings capture the most information from the original data.
2. [🍝 Independent Component Analysis](/public-garden/notes/Machine Learning/Unsupervised Learning/🍝 Independent Component Analysis.html) is similar to PCA but opts to maximize the variance of the projected data instead.

Another way to view dimensionality reduction is by grouping points together; each point can then be represented by the group it belongs to.
1. [🎒 K-Means Clustering](/public-garden/notes/Machine Learning/Unsupervised Learning/🎒 K-Means Clustering.html) groups points into multiple clusters, which each point belonging to exactly one cluster.
2. [📼 Gaussian Mixture Model](/public-garden/notes/Machine Learning/Unsupervised Learning/📼 Gaussian Mixture Model.html) is a generalization of this idea with soft clusters: each point has a probability of belonging to each group.

The models above hidden states that explained some underlying pattern in our data. We can capture these relationships using a [⏰ Bayesian (Belief) Network](/public-garden/notes/Machine Learning/Unsupervised Learning/⏰ Bayesian (Belief) Network.html), which graphically represent complex joint probability distributions. Structuring these networks in certain ways and assigning each node a hidden or observable value, we get more advanced algorithms.
1. [📄 Latent Dirichlet Allocation](/public-garden/notes/Machine Learning/Unsupervised Learning/📄 Latent Dirichlet Allocation.html) expands upon the mixture idea to classify documents, associating hidden topics with each document and word.
2. [⛓️ Markov Chain](/public-garden/notes/Machine Learning/Unsupervised Learning/⛓️ Markov Chain.html) models dynamic systems that transition between states.
3. [☂️ Hidden Markov Model](/public-garden/notes/Machine Learning/Unsupervised Learning/☂️ Hidden Markov Model.html)s convert an input sequence to an output sequence by moving between hidden states.

## Reinforcement Learning
In reinforcement learning, the goal is to learn a policy function \(p(a \vert s)\) that maximizes the agent's total reward. The feedback loop is below. Our environment includes both the game as well as an opponent, if it exists.

<div>
<img src="attachment:notes/Attachments/notes/Attachments/20221229103234.png.png" width="400"/>
</div>

Reward is the result of taking an action at a certain state, \(r(s, a)\). In some games, this is only nonzero at the end (for a win or loss). Most models also have a discount rate \(\gamma\) that decreases the magnitude of future reward; this represents the importance of future gains with respect to current ones.

The sole exception to this format is [🎰 Contextual Bandit](/public-garden/notes/Machine Learning/Reinforcement Learning/🎰 Contextual Bandit.html), which considers only immediate reward, ignoring the action's impact on its state and future reward.

Discounted reward, or long-term return, is defined as 

\[

G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \ldots = \sum_{k=0}^\infty \gamma^k R_{k+t+1}

\]

This idea is captured in \(V_\pi(s_t)\) and \(Q_\pi(s_t, a_t)\), the expected value of a state or state-action pair.
1. For \(V\), expected value is discounted reward starting from \(s_t\) and assuming we act according to policy \(\pi\) in the future.
2. For \(Q\), expected value is discounted reward starting from \(s_t\) and taking action \(a_t\), then assuming we act according to policy \(\pi\) for all moves after \(a_t\).

Learning algorithms optimize \(V\) or \(Q\) values to derive a policy. They can be model-based or model-free: the former learns a model of the world while the latter optimizes itself without it.

Model-based methods explicitly learn about the environment \(p(s_{t+1} \vert s_t, a_t)\) and \(r(s_t, a_t)\). Using this information, they derive a policy.
1. [🌎 Markov Decision Process](/public-garden/notes/Machine Learning/Reinforcement Learning/🌎 Markov Decision Process.html) models the world using states, action transitions, and the resulting reward.
2. [🧨 Dynamic Programming](/public-garden/notes/Machine Learning/Reinforcement Learning/🧨 Dynamic Programming.html) derives the policy by checking the possible moves for each state.

Model-free methods learn \(V\) and \(Q\) by directly playing in the environment.
1. [⏳ Temporal Difference (0)](/public-garden/notes/Machine Learning/Reinforcement Learning/⏳ Temporal Difference (0).html) is a generalized algorithm that iteratively takes a single action and learns better \(V\) or \(Q\) values.
2. [🧭 SARSA](/public-garden/notes/Machine Learning/Reinforcement Learning/🧭 SARSA.html) is a variant of TD(0) that uses on-policy, exploratory updates.
3. [🔭 Q-Learning](/public-garden/notes/Machine Learning/Reinforcement Learning/🔭 Q-Learning.html) is another variant of TD(0) that uses off-policy exploratory actions to optimize a exploitative policy.
4. [🎲 Monte Carlo Tree Search](/public-garden/notes/Machine Learning/Reinforcement Learning/🎲 Monte Carlo Tree Search.html) simulates entire games first before optimizing its values.

[🛸 Deep Q-Learning](/public-garden/notes/Machine Learning/Reinforcement Learning/🛸 Deep Q-Learning.html) is at the intersection of reinforcement learning and deep learning. Whereas SARSA and Q-Learning kept its \(Q(s, a)\) values in a table, it can instead be interpreted as a function captured by a neural network. This generalization provides additional capabilities.
1. We can directly model the policy \(\pi_\theta(a \vert s)\) with a neural network and optimize via policy gradients.
2. Imitation learning learns from the actions a human took at each state and computing a probability distribution via empirical data.
3. Self-play pits the learned policy against itself in games that have opponents.

One slightly different style of reinforcement learning, bridging the gap with active learning, is [🚒 Response Surface Methods](/public-garden/notes/Machine Learning/Reinforcement Learning/🚒 Response Surface Methods.html), used to sample points for some objective