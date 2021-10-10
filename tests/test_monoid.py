import functools
import operator

from category_theory import fold
from category_theory import foldr
from category_theory import monoid


def test_IntPlus():
    values = [1, 2, 3]
    value = fold((monoid.IntPlus(v) for v in values), monoid.IntPlus)
    assert value == sum(values)


def test_IntProd():
    values = [1, 2, 3]
    value = fold((monoid.IntProd(v) for v in values), monoid.IntProd)
    assert value == functools.reduce(operator.mul, values)


def test_MaybeIntPlus():
    values = [1, None, 3]
    value = fold((monoid.MaybeIntPlus(v) for v in values), monoid.MaybeIntPlus)
    assert value.value is None


def test_String_fold():
    values = ["H", "e", "l", "l", "o"]
    value = fold((monoid.String(v) for v in values), monoid.String)
    assert value == "".join(values)


def test_String_foldr():
    values = ["H", "e", "l", "l", "o"]
    value = foldr((monoid.String(v) for v in values), monoid.String)
    assert value == "".join(values)
