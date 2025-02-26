from math import sin
from scipy.differentiate import derivative
import numpy as np

EPS = 0.001

INTERVAL_L = 0.0
INTERVAL_R = 1.0


def f(x: np.ndarray) -> np.ndarray:
    return x**3 - 3 * np.sin(x)


# ---
def fn(x: float) -> float:
    return x**3 - 3 * sin(x)


def df(x: float) -> float:
    return derivative(f, x)["df"]


def d2f(x: float) -> float:
    # TODO
    return 6 * x + 3 * sin(x)
