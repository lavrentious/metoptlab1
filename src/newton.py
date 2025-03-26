from typing import Callable
from utils import EPS


def newton(
    fn: Callable[[float], float],
    df: Callable[[float], float],
    d2f: Callable[[float], float],
    a: float,
    b: float,
    eps: float = EPS,
) -> float:
    """
    returns xm
    """

    xk = (a + b) / 2
    while abs(df(xk)) >= eps:
        xk = xk - df(xk) / d2f(xk)
    return xk
