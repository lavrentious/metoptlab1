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
            print(f"\nИтерация {iteration}:")
            print(f"x1 = {x1}\tf1 = {f1}")
            print(f"x2 = {x2}\tf2 = {f2}")
            print(f"x3 = {x3}\tf3 = {f3}")

        if denom == 0:
            if verbose:
                print("Знаменатель равен 0, пересчет точек")
            x1, f1, x2, f2, x3, f3 = get_x1_x2_x3(xmin)
            continue

        xline = 0.5 * num / denom
        fline = fn(xline)

        if verbose:
            print(f"xmin = {xmin} ; fmin = {fmin}")
            print(f"xline = {xline} ; fline = {fline}")
            print(f"|(fmin - fline) / fline| = {abs((fmin - fline) / fline)}")
            print(f"|(xmin - xline) / xline| = {abs((xmin - xline) / xline)}")

        cond1 = abs((fmin - fline) / fline) < eps1
        cond2 = abs((xmin - xline) / xline) < eps2
        xs = [x1, x2, x3, xline]
        if cond1 and cond2:
            if verbose:
                print(f"Результат: x*={xline}")
            return xline
        elif min(x1, x2, x3) <= xline <= max(x1, x2, x3):
            x2 = min(xmin, xline, key=lambda x: fn(x))
            x1 = max(filter(lambda x: x < x2, xs))
            x3 = min(filter(lambda x: x > x2, xs))
            f1, f2, f3 = fn(x1), fn(x2), fn(x3)
        else:
            x1, f1, x2, f2, x3, f3 = get_x1_x2_x3(xline)

    if verbose:
        print("Достигнуто максимальное число итераций, возвращается -1")
    return -1
