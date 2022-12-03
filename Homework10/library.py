import functools


@functools.cache
def multiply_then_expo(factor1: int | float, factor2: int | float, /, *, exponent: int | float) -> int | float:
    if (factor1 * factor2) < 0 and -1 < exponent < 1 and exponent != 0 and 1 / exponent % 2 == 0:
        raise ValueError
    res = (factor1 * factor2) ** exponent
    return res
