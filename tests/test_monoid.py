import functools
import itertools
import operator

import pytest
from category_theory import monoid
from category_theory import operations as op
from category_theory import par_operations as parop
from hypothesis import given
from hypothesis import settings
from hypothesis import strategies as st


@pytest.mark.parametrize("cls", [monoid.IntPlus, monoid.IntProd, monoid.MaybeIntPlus])
@given(st.integers(), st.integers(), st.integers())
def test_integer_Monoid_is_associative(cls, a_, b_, c_):
    a = cls(a_)
    b = cls(b_)
    c = cls(c_)
    assert a + (b + c) == (a + b) + c == a + b + c


@pytest.mark.parametrize("cls", [monoid.All, monoid.Any])
@given(st.booleans(), st.booleans(), st.booleans())
def test_boolean_Monoid_is_associative(cls, a_, b_, c_):
    a = cls(a_)
    b = cls(b_)
    c = cls(c_)
    assert a + (b + c) == (a + b) + c == a + b + c


@given(st.text(), st.text(), st.text())
def test_String_is_associative(a_, b_, c_):
    a = monoid.String(a_)
    b = monoid.String(b_)
    c = monoid.String(c_)
    assert a + (b + c) == (a + b) + c == a + b + c


@pytest.mark.parametrize("cls", [monoid.IntPlus, monoid.IntProd, monoid.MaybeIntPlus])
@given(st.integers())
def test_integer_Monoid_identity(cls, a_):
    a = cls(a_)
    e = cls.e()
    assert a + e == e + a == a


@pytest.mark.parametrize("cls", [monoid.All, monoid.Any])
@given(st.booleans())
def test_boolean_Monoid_identity(cls, a_):
    a = cls(a_)
    e = cls.e()
    assert a + e == e + a == a


@given(st.text())
def test_String_identity(a_):
    a = monoid.String(a_)
    e = monoid.String.e()
    assert a + e == e + a == a


@pytest.mark.parametrize("cls", [monoid.IntPlus, monoid.MaybeIntPlus])
@given(st.iterables(st.integers()))
def test_IntPlus_fold(cls, values):
    values, values_copy = itertools.tee(values)
    value = op.fold((cls(v) for v in values), cls)
    assert value == cls(sum(values_copy))


def test_IntPlus_par():
    values = list(range(100 * 5))
    value = parop.fold(
        (monoid.IntPlus(v) for v in values),
        monoid.IntPlus,
        chunk_size=99,
    ).compute()
    assert value == monoid.IntPlus(sum(values))


@pytest.mark.parametrize("cls", [monoid.IntProd, monoid.MaybeIntProd])
@given(st.iterables(st.integers()))
def test_IntProd_fold(cls, values):
    values, values_copy = itertools.tee(values)
    value = op.fold((cls(v) for v in values), cls)
    assert value == cls(functools.reduce(operator.mul, values_copy, cls.e().value))


def test_MaybeIntPlus():
    values = [1, None, 3]
    value = op.fold((monoid.MaybeIntPlus(v) for v in values), monoid.MaybeIntPlus)
    assert value == monoid.MaybeIntPlus(None)


@given(st.iterables(st.booleans()))
def test_All_fold(values):
    values, values_copy = itertools.tee(values)
    value = op.fold((monoid.All(v) for v in values), monoid.All)
    assert value == monoid.All(all(values_copy))


@given(st.iterables(st.booleans()))
def test_Any_fold(values):
    values, values_copy = itertools.tee(values)
    value = op.fold((monoid.Any(v) for v in values), monoid.Any)
    assert value == monoid.Any(any(values_copy))


@pytest.mark.parametrize(
    "cls, func",
    itertools.product((monoid.String,), (op.fold, op.foldr)),
)
@given(st.iterables(st.text()))
def test_String_fold(cls, func, values):
    values, values_copy = itertools.tee(values)
    value = func((cls(v) for v in values), cls)
    assert value == cls("".join(values_copy))


@given(st.lists(st.text()), st.integers(min_value=1))
@settings(max_examples=100)
def test_String_par_fold(values, chunk_size):
    chunk_size = max(min(chunk_size, len(values)), 1)
    value = parop.fold(
        (monoid.String(v) for v in values),
        monoid.String,
        chunk_size=chunk_size,
    ).compute()
    assert value == monoid.String("".join(values))
