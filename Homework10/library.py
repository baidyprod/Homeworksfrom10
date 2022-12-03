import functools


@functools.cache
def multiply_then_expo(factor1: int | float, factor2: int | float, /, *, exponent: int | float) -> int | float:
    if (factor1 * factor2) < 0 and -1 < exponent < 1 and exponent != 0 and 1 / exponent % 2 == 0:
        # When exponent value is between -1 and 1, it is equal to take a root.
        # Even root can't be extracted when there is a negative number under it.
        # So the function raises ValueError.
        raise ValueError
    res = (factor1 * factor2) ** exponent
    return res
