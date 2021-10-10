import functools
import operator

import pytest
from category_theory import fold
from category_theory import foldr
from category_theory import monoid
from category_theory import par_fold
from hypothesis import given
from hypothesis import strategies as st


@pytest.mark.parametrize("cls", [monoid.IntPlus, monoid.IntProd, monoid.MaybeIntPlus])
@given(st.integers(), st.integers(), st.integers())
def test_integer_Monoid_is_associative(cls, a_, b_, c_):
    a = cls(a_)
    b = cls(b_)
    c = cls(c_)
    assert a + (b + c) == (a + b) + c == a + b + c


@pytest.mark.parametrize("cls", [monoid.IntPlus, monoid.IntProd, monoid.MaybeIntPlus])
@given(st.integers())
def test_integer_Monoid_identity(cls, a_):
    a = cls(a_)
    e = cls.e()
    assert a + e == e + a == a


def test_IntPlus():
    values = [1, 2, 3]
    value = fold((monoid.IntPlus(v) for v in values), monoid.IntPlus)
    assert value == monoid.IntPlus(sum(values))


def test_IntPlus_par():
    values = list(range(100 * 5))
    value = par_fold(
        (monoid.IntPlus(v) for v in values),
        monoid.IntPlus,
        chunk_size=99,
    ).compute()
    assert value == monoid.IntPlus(sum(values))


def test_IntProd():
    values = [1, 2, 3]
    value = fold((monoid.IntProd(v) for v in values), monoid.IntProd)
    assert value == monoid.IntProd(functools.reduce(operator.mul, values))


def test_MaybeIntPlus():
    values = [1, None, 3]
    value = fold((monoid.MaybeIntPlus(v) for v in values), monoid.MaybeIntPlus)
    assert value == monoid.MaybeIntPlus(None)


def test_String_fold():
    values = ["H", "e", "l", "l", "o"]
    value = fold((monoid.String(v) for v in values), monoid.String)
    assert value == monoid.String("".join(values))


def test_String_foldr():
    values = ["H", "e", "l", "l", "o"]
    value = foldr((monoid.String(v) for v in values), monoid.String)
    assert value == monoid.String("".join(values))


def test_String_par_fold():
    values = ["H", "e", "l", "l", "o"] * 100
    value = par_fold(
        (monoid.String(v) for v in values),
        monoid.String,
        chunk_size=99,
    ).compute()
    assert value == monoid.String("".join(values))
