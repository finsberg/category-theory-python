import functools
import operator

from category_theory import fold
from category_theory import foldr
from category_theory import monoid
from category_theory import par_fold


def test_IntPlus():
    values = [1, 2, 3]
    value = fold((monoid.IntPlus(v) for v in values), monoid.IntPlus)
    assert value == sum(values)


def test_IntPlus_par():
    values = list(range(100 * 5))
    value = par_fold(
        (monoid.IntPlus(v) for v in values),
        monoid.IntPlus,
        chunk_size=100,
    ).compute()
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


def test_String_par_fold():
    values = ["H", "e", "l", "l", "o"] * 100
    value = par_fold(
        (monoid.String(v) for v in values),
        monoid.String,
        chunk_size=99,
    ).compute()
    assert value == "".join(values)
