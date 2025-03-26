from typing import Callable
from utils import EPS


def golden_ratio(
    fn: Callable[[float], float], a: float, b: float, eps: float = EPS
) -> float:
    i = 0

    def calc(
        a: float, b: float, x1: float | None = None, x2: float | None = None
    ) -> float:
        nonlocal i
        if b - a < eps:
            return (a + b) / 2
        if x1 is None:
            x1 = a + 0.382 * (b - a)
        if x2 is None:
            x2 = a + 0.618 * (b - a)
        print(i, a, b, x1, x2, fn(x1), fn(x2), "<" if fn(x1) < fn(x2) else ">")
        i += 1
        if fn(x1) < fn(x2):
            return calc(a, x2, None, x1)
        else:
            return calc(x1, b, x2, None)

    return calc(a, b)
