import importlib.util
import sys
from pathlib import Path

import numpy as np

_SPEC = importlib.util.spec_from_file_location(
    "gradient_descent", Path(__file__).resolve().parent / "gradient_descent.py"
)
gd = importlib.util.module_from_spec(_SPEC)
sys.modules["gradient_descent"] = gd
_SPEC.loader.exec_module(gd)


def make_linear_dataset(n: int = 200, d: int = 3, seed: int = 0):
    rng = np.random.default_rng(seed)
    X = rng.normal(size=(n, d))
    true_w = np.array([2.0, -1.0, 0.5])
    true_b = 4.0
    noise = rng.normal(scale=0.1, size=n)
    y = X @ true_w + true_b + noise
    return X, y, true_w, true_b


def test_mse_zero_for_perfect_prediction():
    y = np.array([1.0, 2.0, 3.0])
    assert gd.mse(y, y) == 0.0


def test_fit_gradient_descent_converges_toward_true_weights():
    X, y, true_w, true_b = make_linear_dataset()
    w, b, loss_history = gd.fit_gradient_descent(X, y, lr=0.1, iterations=500)

    assert np.allclose(w, true_w, atol=0.1)
    assert abs(b - true_b) < 0.1


def test_loss_decreases_monotonically_on_average():
    X, y, _, _ = make_linear_dataset()
    _, _, loss_history = gd.fit_gradient_descent(X, y, lr=0.1, iterations=500)

    assert loss_history[-1] < loss_history[0]
    # average loss over the back half should be much lower than the front half
    midpoint = len(loss_history) // 2
    assert np.mean(loss_history[midpoint:]) < np.mean(loss_history[:midpoint])


def test_predict_matches_fitted_weights():
    X, y, _, _ = make_linear_dataset()
    w, b, _ = gd.fit_gradient_descent(X, y, lr=0.1, iterations=500)
    preds = gd.predict(X, w, b)
    assert gd.mse(y, preds) < 0.1
