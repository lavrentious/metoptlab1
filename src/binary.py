from typing import Callable

from utils import EPS


def binary_search(
    fn: Callable[[float], float],
    a: float,
    b: float,
    eps: float = EPS,
    verbose: bool = False,
) -> float:
    """
    returns xm
    """
    i = 0
    while (b - a) > 2 * eps:
        x1 = (a + b - eps) / 2
        y1 = fn(x1)
        x2 = (a + b + eps) / 2
        y2 = fn(x2)

        if verbose:
            print(
                f"Шаг {i}: a={a:.6f}, b={b:.6f}, x1={x1:.6f}, y1={y1:.6f}, x2={x2:.6f}, y2={y2:.6f}"
            )

        if y1 > y2:
            if verbose:
                print(f"y1 > y2, сдвигаем a -> {x1:.6f}")
            a = x1
        else:
            if verbose:
                print(f"y1 <= y2, сдвигаем b -> {x2:.6f}")
            b = x2

        i += 1

    xm = (a + b) / 2
    return xm
