import functools
import operator

from category_theory import monoid


def test_IntPlus():
    values = [1, 2, 3]
    value = monoid.squash((monoid.IntPlus(v) for v in values), monoid.IntPlus)
    assert value == sum(values)


def test_IntProd():
    values = [1, 2, 3]
    value = monoid.squash((monoid.IntProd(v) for v in values), monoid.IntProd)
    assert value == functools.reduce(operator.mul, values)


def test_MaybeIntPlus():
    values = [1, None, 3]
    value = monoid.squash((monoid.MaybeIntPlus(v) for v in values), monoid.MaybeIntPlus)
    assert value.value is None
