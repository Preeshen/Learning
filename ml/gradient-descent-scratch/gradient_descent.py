"""Linear regression via gradient descent, from scratch — no autograd, no scikit-learn.

Compared against scikit-learn's closed-form OLS fit in benchmarks.json (day 10's measurement).
"""

from __future__ import annotations

import numpy as np


def mse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    raise NotImplementedError


def fit_gradient_descent(
    X: np.ndarray, y: np.ndarray, lr: float = 0.01, iterations: int = 1000
) -> tuple[np.ndarray, float, list[float]]:
    """Fit y = X @ w + b by gradient descent on mean squared error.

    Return (weights, bias, loss_history). O(iterations * n * d) time, O(n) extra space.
    """
    raise NotImplementedError


def predict(X: np.ndarray, w: np.ndarray, b: float) -> np.ndarray:
    raise NotImplementedError
