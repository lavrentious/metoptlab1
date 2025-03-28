from typing import Callable

from utils import EPS


def golden_ratio(
    fn: Callable[[float], float],
    a: float,
    b: float,
    eps: float = EPS,
    verbose: bool = False,
) -> float:
    i = 0

    def calc(
        a: float,
        b: float,
        x1: float | None = None,
        x2: float | None = None,
    ) -> float:
        nonlocal i
        i += 1
        if b - a < eps:
            return (a + b) / 2

        if x1 is None:
            x1 = a + 0.382 * (b - a)
        if x2 is None:
            x2 = a + 0.618 * (b - a)

        y1, y2 = fn(x1), fn(x2)
        if verbose:
            print(
                f"Шаг {i}: a={a:.6f}, b={b:.6f}, x1={x1:.6f}, y1={y1:.6f}, x2={x2:.6f}, y2={y2:.6f}"
            )

        if y1 < y2:
            if verbose:
                print(f"y1 < y2, сдвигаем b -> {x2:.6f}")
            return calc(a, x2, None, x1)
        else:
            if verbose:
                print(f"y1 >= y2, сдвигаем a -> {x1:.6f}")
            return calc(x1, b, x2, None)

    return calc(a, b)
