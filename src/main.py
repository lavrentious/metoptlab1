from typing import Callable

from argparser import ArgParser
from binary import binary_search
from chord import chord
from golden_ratio import golden_ratio
from newton import newton
from quadratic_approximation import quadratic_approximation
from utils import INTERVAL_L, INTERVAL_R, d2f, df, fn


def print_result(
    fn: Callable[[float], float],
    solve_fn: Callable[[Callable[[float], float], float, float], float],
) -> None:
    xm = solve_fn(fn, INTERVAL_L, INTERVAL_R)
    ym = fn(xm)
    print(f"xm = {xm}, ym = {ym}")


argparser = ArgParser()
argparser.parse_and_validate_args()
VERBOSE = argparser.verbose


print("1.1. Метод дихотомии:")
print_result(fn, lambda f, a, b: binary_search(f, a, b, verbose=argparser.verbose))

print("\n1.2. Метод золотого сечения:")
print_result(fn, lambda f, a, b: golden_ratio(f, a, b, verbose=argparser.verbose))

print("\n1.3. Метод хорд:")
print_result(fn, lambda f, a, b: chord(f, df, a, b, verbose=argparser.verbose))

print("\n1.4. Метод Ньютона:")
print_result(fn, lambda f, a, b: newton(f, df, d2f, a, b, verbose=argparser.verbose))

print("\n2.1 Метод квадратичной аппроксимации:")
print_result(
    fn, lambda f, a, b: quadratic_approximation(f, a, b, verbose=argparser.verbose)
)
