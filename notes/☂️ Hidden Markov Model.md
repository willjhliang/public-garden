---
title: "☂️ Hidden Markov Model"
---
# Theory
Hidden Markov Models use the Markov property, which states that each variable conditionally depends only on the variable right before it in the sequence.
$$p(x_1, x_2, x_3, x_4) = p(x_1)p(x_2|x_1)p(x_3|x_2)p(x_4|x_3)$$
We exploit this assumption to translate an input sequence to another sequence using a Markov matrix or graph that models probabilistic transitions across variables. The graph consists of hidden states and observable variables in the structure below; note that this structure is similar to [[⛓️ Markov Chain]] with observable variables tacked onto the original states.

![[400]]
Each hidden state gives emissions with certain probabilities and transition to another hidden state with another set of probabilities. The input sequence we get is the observable variables $Y$, and for translation, our goal is to find the most probable sequence $X$ that generated these emissions.

To predict the probability of sequence $X$ given another sequence $Y$, we use [[Y) = \arg\max_X \frac{P(Y|X)P(X)}{P(Y)} = \arg\max_X \prod_{i=1}^m P(y_i|x_i) P(x_i|x_{i-1})$$

For example, for speech recognition (predicting words from sounds), we start with a prior of the likelihood of each word along with likelihood of each sound given a word.

# Model
Our model consists of hidden states $X$, transition probabilities $p(x_i|x_j) = A_{ij}$ in the Markov transition matrix, and observation emission for each state $p(y_j | x_i) = B_{ij}$.

We also track an initial state distribution, $p(x_i) = \pi_i$ to determine which state to start in.

# Training
Given training data $D$, we maximize $P(D|\lambda)$ for parameters $\lambda = (A, B, \pi)$ using [[🎉 Expectation Maximization]].

# Prediction
There are two main types of problems with HMMs.
1. Evaluation: given observations $Y$ and $\lambda = (A, B, \pi)$, compute probability of $Y$ occurring.
2. Decoding: given observations $Y$ and $\lambda = (A, B, \pi)$, find the state sequence $X$ that best explains $Y$; in other words, find the sequence that has highest probability of generating $Y$ using the Bayes' rule equation above.