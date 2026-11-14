"""Linear regression via gradient descent, from scratch — no autograd, no scikit-learn.

Compared against scikit-learn's closed-form OLS fit in benchmarks.json (day 10's measurement).
"""

from __future__ import annotations

import numpy as np


def mse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean((y_true - y_pred) ** 2))


def fit_gradient_descent(
    X: np.ndarray, y: np.ndarray, lr: float = 0.01, iterations: int = 1000
) -> tuple[np.ndarray, float, list[float]]:
    """Fit y = X @ w + b by gradient descent on mean squared error.

    Returns (weights, bias, loss_history). O(iterations * n * d) time, O(n) extra space.
    """
    n, d = X.shape
    w = np.zeros(d)
    b = 0.0
    loss_history: list[float] = []

    for _ in range(iterations):
        y_pred = X @ w + b
        error = y_pred - y
        loss_history.append(mse(y, y_pred))

        grad_w = (2.0 / n) * (X.T @ error)
        grad_b = (2.0 / n) * np.sum(error)

        w -= lr * grad_w
        b -= lr * grad_b

    return w, b, loss_history


def predict(X: np.ndarray, w: np.ndarray, b: float) -> np.ndarray:
    return X @ w + b
