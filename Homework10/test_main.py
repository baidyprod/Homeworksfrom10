from library import multiply_then_expo


def test_typeerror():
    assert type(multiply_then_expo('1', 3, exponent=2)) == int, 'Typeerror: not int'


def test_valueerror():
    assert multiply_then_expo('1', 3, exponent=2), 'Valueerror: not int'


def test_negative_by_odd_exp():
    assert (multiply_then_expo(-2, 3, exponent=2)) > 0, 'Should be positive'

