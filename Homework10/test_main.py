from library import multiply_then_expo
import pytest


def test_typeerror():
    with pytest.raises(TypeError):
        multiply_then_expo('1', 3, exponent=2)


def test_valueerror():
    with pytest.raises(ValueError):
        multiply_then_expo(-1, 3, exponent=0.5)


def test_negative_by_odd_exp():
    assert multiply_then_expo(-2, 3, exponent=2) > 0, 'Should be positive'


@pytest.mark.parametrize('a, b, exp', [(1, 1, 0), (2, 5, 0), (-2, 5, 0)])
def test_by_zero_exp(a, b, exp):
    assert multiply_then_expo(a, b, exponent=exp) == 1
