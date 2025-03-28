from typing import Callable

from utils import EPS


def newton(
    fn: Callable[[float], float],
    df: Callable[[float], float],
    d2f: Callable[[float], float],
    a: float,
    b: float,
    eps: float = EPS,
    verbose: bool = False,
) -> float:
    """
    returns xm
    """
    i = 0
    xk = (a + b) / 2
    while abs(df(xk)) >= eps:

        if verbose:
            print(f"Шаг {i}: xk={xk:.6f}, df(xk)={df(xk):.6f}, d2f(xk)={d2f(xk):.6f}")

        assert d2f(xk) != 0, "d2f(xk) == 0, метод Ньютона неприменим"

        xk = xk - df(xk) / d2f(xk)

        i += 1
    return xk
