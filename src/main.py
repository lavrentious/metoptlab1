from utils import fn, df, d2f, INTERVAL_L, INTERVAL_R
from binary import binary_search
from golden_ratio import golden_ratio
from typing import Callable
from chord import chord
from newton import newton


def print_result(
    fn: Callable[[float], float],
    solve_fn: Callable[[Callable[[float], float], float, float], float],
):
    xm = solve_fn(fn, INTERVAL_L, INTERVAL_R)
    ym = fn(xm)
    print(f"xm = {xm}, ym = {ym}")


# print("1.1. Метод дихотомии:")
# print_result(fn, binary_search)

# print("\n1.2. Метод золотого сечения:")
# print_result(fn, golden_ratio)

print("\n1.3. Метод хорд:")
print_result(fn, lambda f, a, b: chord(f, df, a, b))

# print("\n1.4. Метод Ньютона:")
# print_result(fn, lambda f, a, b: newton(f, df, d2f, a, b))
