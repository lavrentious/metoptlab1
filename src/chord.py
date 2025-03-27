from typing import Callable

from utils import EPS


def chord(
    fn: Callable[[float], float],
    df: Callable[[float], float],
    a: float,
    b: float,
    eps: float = EPS,
    verbose: bool = False,
) -> float:
    """
    returns xm
    """

    i = 0
    while True:
        xt = a - (a - b) * df(a) / (df(a) - df(b))
        df_xt = df(xt)

        if verbose:
            print(f"Шаг {i}: a={a:.6f}, b={b:.6f}, xt={xt:.6f}, f'(xt)={df_xt:.6f}")

        if df_xt > 0:
            if verbose:
                print(f"f'(xt) > 0, сдвигаем b -> {xt:.6f}")
            b = xt
        else:
            if verbose:
                print(f"f'(xt) <= 0, сдвигаем a -> {xt:.6f}")
            a = xt

        if abs(df_xt) < eps:
            return xt

        i += 1
