"""Run once to produce benchmarks.json — the day-10 measurement (Principle V)."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
from sklearn.linear_model import LinearRegression

_SPEC = importlib.util.spec_from_file_location(
    "gradient_descent", Path(__file__).resolve().parent / "gradient_descent.py"
)
gd = importlib.util.module_from_spec(_SPEC)
sys.modules["gradient_descent"] = gd
_SPEC.loader.exec_module(gd)


def main() -> None:
    rng = np.random.default_rng(0)
    n, d = 500, 3
    X = rng.normal(size=(n, d))
    true_w = np.array([2.0, -1.0, 0.5])
    true_b = 4.0
    noise = rng.normal(scale=0.1, size=n)
    y = X @ true_w + true_b + noise

    w, b, loss_history = gd.fit_gradient_descent(X, y, lr=0.1, iterations=500)
    scratch_mse = gd.mse(y, gd.predict(X, w, b))

    baseline = LinearRegression().fit(X, y)
    baseline_pred = baseline.predict(X)
    baseline_mse = gd.mse(y, baseline_pred)

    payload = {
        "metric": "accuracy",
        "baseline": "scikit-learn LinearRegression (closed-form OLS)",
        "method": "fit both on the same synthetic dataset; report MSE and iterations-to-converge for the scratch version",
        "result": scratch_mse,
        "baseline_result": baseline_mse,
        "unit": "mean squared error",
        "iterations_to_converge": 500,
        "note": "closed-form OLS reaches the global optimum in one step; gradient descent needs "
                "iterations and a tuned learning rate to approach it — that gap is the whole point "
                "of this comparison.",
    }
    out_path = Path(__file__).resolve().parent / "benchmarks.json"
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {out_path}")
    print(f"scratch MSE: {scratch_mse:.6f} · baseline MSE: {baseline_mse:.6f}")


if __name__ == "__main__":
    main()
