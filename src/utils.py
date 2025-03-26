from math import sin

EPS = 0.0001

INTERVAL_L = 0.0
INTERVAL_R = 1.0


def fn(x: float) -> float:
    return x**3 - 3 * sin(x)


# def df(x: float) -> float:
#     return derivative(f, x)["df"]


# def d2f(x: float) -> float:
#     # TODO
#     return 6 * x + 3 * sin(x)


def df(x: float) -> float:
    H = 0.0001
    return (fn(x + H) - fn(x - H)) / (2 * H)


def d2f(x: float) -> float:
    H = 0.0001
    return (fn(x + H) - 2 * fn(x) + fn(x - H)) / H**2
