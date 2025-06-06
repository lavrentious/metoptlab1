from typing import Callable

from argparser import ArgParser
from solvers.binary import binary_search
from solvers.chord import chord
from solvers.golden_ratio import golden_ratio
from solvers.newton import newton
from solvers.quadratic_approximation import quadratic_approximation
from utils import INTERVAL_L, INTERVAL_R, d2f, df, fn


def run() -> None:
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
    print_result(
        fn,
        lambda f, a, b: chord(f, lambda x: df(f, x), a, b, verbose=argparser.verbose),
    )

    print("\n1.4. Метод Ньютона:")
    print_result(
        fn,
        lambda f, a, b: newton(
            f, lambda x: df(f, x), lambda x: d2f(f, x), a, b, verbose=argparser.verbose
        ),
    )

    print("\n2.1 Метод квадратичной аппроксимации:")
    print_result(
        fn, lambda f, a, b: quadratic_approximation(f, a, b, verbose=argparser.verbose)
    )


if __name__ == "__main__":
    run()
