import functools


@functools.cache
def multiply_then_expo(factor1: int, factor2: int, /, *, exponent: int) -> int:
    res = (factor1 * factor2) ** exponent
    return res
