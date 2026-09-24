# Sparsity Promotion Through $\ell_0$-penalties
In many applications it is desired to incentivize sparse solutions, that is solutions with fewer variables which take nonzero values.
In order to do this one can employ an $\ell_0$ penalty, where the 0-norm is defined as the number of non-zero elements in a vector.
These kinds of problems can be reformulated both as MPCCs which can be solved to local optimality cheaply, and MINLPs, which can be solved to global optimality, albeit much more expensively.

## Application: Sparse Portfolio Optimization
One basic example of such a problem is Sparse portfolio optimization.
The goal of this problem is to choose a sufficiently sparse portfolio of assets, given a covariance matrix $Q$ and a return vector $\mu$.
A further description of this problem formulation can be found in [section 5.1.1 of this article](https://arxiv.org/pdf/2509.03203).
An explanation of the MIQP reformulation is also found in that section.
For an explanation of how to reformulate $\ell_0$-norm penalties using complementarities can be found in [this article](https://www.math.uwaterloo.ca/~mbfeng/papers/2018_L0Opt.pdf).

## Task:
We have provided a template of an implementation for modelling and solving such a problem.
It is your task in this exercise to finish this implementation and compare the performance of the local and global solutions.
Take particular note of the differences in compute time scaling, and the objective gaps you observe. 