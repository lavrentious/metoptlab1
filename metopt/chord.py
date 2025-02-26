from typing import Callable, List
from utils import EPS


def chord(
    fn: Callable[[float], float],
    df: Callable[[float], float],
    a: float,
    b: float,
    eps=EPS,
) -> float:
    """
    returns xm
    """

    while True:
        xt = a - (a - b) * df(a) / (df(a) - df(b))
        if df(xt) > 0:
            b = xt
        else:
            a = xt
        if abs(df(xt)) < eps:
            return xt
