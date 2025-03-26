from typing import Callable, List
from utils import EPS


def binary_search(fn: Callable[[float], float], a: float, b: float, eps=EPS) -> float:
    """
    returns xm
    """
    while (b - a) > 2 * eps:
        x1 = (a + b - eps) / 2
        y1 = fn(x1)
        x2 = (a + b + eps) / 2
        y2 = fn(x2)
        if y1 > y2:
            a = x1
        else:
            b = x2
    return (a + b) / 2
