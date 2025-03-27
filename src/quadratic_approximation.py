from typing import Callable, Tuple

from utils import EPS, QA_STEP

MAX_ITERATIONS = 100


def quadratic_approximation(
    fn: Callable[[float], float],
    a: float,
    b: float,
    eps1: float = EPS,
    eps2: float = EPS,
    verbose: bool = False,
) -> float:
    """
    returns x*
    """

    def get_x1_x2_x3(x1: float) -> Tuple[float, float, float, float, float, float]:
        x2 = x1 + QA_STEP
        f1, f2 = fn(x1), fn(x2)
        if f1 > f2:
            x3 = x1 + 2 * QA_STEP
        else:
            x3 = x1 - QA_STEP
        f3 = fn(x3)
        return x1, f1, x2, f2, x3, f3

    # определение стартовых точек
    x1, f1, x2, f2, x3, f3 = get_x1_x2_x3((a + b) / 2)

    for iteration in range(MAX_ITERATIONS):
        # нахождение fmin и xmin
        fmin, xmin = min(zip([f1, f2, f3], [x1, x2, x3]), key=lambda x: x[0])

        # xline = num/denom
        num = (x2**2 - x3**2) * f1 + (x3**2 - x1**2) * f2 + (x1**2 - x2**2) * f3
        denom = (x2 - x3) * f1 + (x3 - x1) * f2 + (x1 - x2) * f3

        if verbose:
            print(
                f"Итерация {iteration}: x1={x1:.6f}, f1={f1:.6f}, x2={x2:.6f}, f2={f2:.6f}, x3={x3:.6f}, f3={f3:.6f}"
            )

        if denom == 0:
            if verbose:
                print("Знаменатель равен 0, пересчет точек")
            x1, f1, x2, f2, x3, f3 = get_x1_x2_x3(xmin)
            continue

        xline = 0.5 * num / denom
        fline = fn(xline)

        if verbose:
            print(
                f"xline={xline:.6f}, fline={fline:.6f}, fmin={fmin:.6f}, xmin={xmin:.6f}"
            )

        cond1 = abs((fmin - fline) / fline) < eps1
        cond2 = abs((xmin - xline) / xline) < eps2
        if cond1 and cond2:
            if verbose:
                print(f"Результат: x*={xline:.6f}")
            return xline
        elif x1 <= xline <= x3:
            x2 = min(xline, xmin)
            x1, x3 = x2 - QA_STEP, x2 + QA_STEP
            f1, f2, f3 = fline, fn(x2), fn(x3)
        else:
            x1, f1, x2, f2, x3, f3 = get_x1_x2_x3(xline)

    if verbose:
        print("Достигнуто максимальное число итераций, возвращается -1")
    return -1
