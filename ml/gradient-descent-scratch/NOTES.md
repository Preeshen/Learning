# Gradient descent & linear regression from scratch

**Problem it solves**: fitting a linear model's parameters to data by iteratively reducing
prediction error, as opposed to solving for the optimum directly.

**Mechanism**: compute the gradient of mean squared error with respect to weights and bias, then
step the parameters in the opposite direction, scaled by a learning rate. Repeat until the loss
stops meaningfully decreasing. For linear regression specifically, a closed-form solution
(ordinary least squares) also exists — gradient descent is the general-purpose tool that still
works when no closed form exists (e.g., for neural networks).

**Failure modes**: a learning rate that's too high causes the loss to oscillate or diverge instead
of decreasing; too low and it converges so slowly that 500 iterations isn't enough. The benchmark
run converged to MSE 0.010587 — matching scikit-learn's closed-form fit to 6 decimal places on
this dataset — which only happened because the learning rate (0.1) and iteration count (500) were
tuned; an untuned run at lr=0.5 diverges on the same data.

**Trade-offs**: closed-form OLS reaches the global optimum in one matrix solve; gradient descent
needs hundreds of iterations and a tuned learning rate to approach it. The entire value of this
exercise is seeing that gap directly: `benchmarks.json` records that gradient descent *can* match
the closed-form answer, but only with real iteration and tuning cost that the closed-form solution
skips entirely. That cost is exactly why neural networks — which have no closed form — need
gradient descent and all its tuning headaches (learning rate schedules, momentum, etc.).
