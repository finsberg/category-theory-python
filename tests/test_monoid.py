import functools
import itertools
import operator

import pytest
from category_theory import monoid
from category_theory import operations as op
from category_theory import par_operations as parop
from hypothesis import given
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


@pytest.mark.parametrize(
    "cls",
    [monoid.IntPlus, monoid.IntProd, monoid.MaybeIntPlus, monoid.MaybeIntProd],
)
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


@pytest.mark.parametrize("func", [op.fold, op.foldr])
@given(st.iterables(st.integers()))
def test_IntPlus_fold(func, values):
    values, values_copy = itertools.tee(values)
    value = func((monoid.IntPlus(v) for v in values), monoid.IntPlus)
    assert value == monoid.IntPlus(sum(values_copy))


@st.composite
def maybeint(draw, elements=st.integers()):
    values = draw(st.lists(elements))
    index = draw(st.integers(min_value=0, max_value=max(len(values) - 1, 0)))
    maybe = draw(st.one_of(st.integers(), st.none()))
    if len(values) > 0:
        values[index] = maybe
    return values


@pytest.mark.parametrize("func", [op.fold, op.foldr])
@given(maybeint())
def test_MaybeIntPlus_fold(func, values):
    value = func((monoid.MaybeIntPlus(v) for v in values), monoid.MaybeIntPlus)
    if None in values:
        true_value = None
    else:
        true_value = sum(values)
    assert value == monoid.MaybeIntPlus(true_value)


@pytest.mark.parametrize("func", [op.fold, op.foldr])
@given(maybeint())
def test_MaybeIntProd_fold(func, values):
    value = func((monoid.MaybeIntProd(v) for v in values), monoid.MaybeIntProd)
    if None in values:
        true_value = None
    else:
        true_value = functools.reduce(
            operator.mul,
            values,
            monoid.MaybeIntProd.e().value,
        )
    assert value == monoid.MaybeIntProd(true_value)


def test_IntPlus_par():
    values = list(range(100 * 5))
    value = parop.fold(
        (monoid.IntPlus(v) for v in values),
        monoid.IntPlus,
        chunk_size=99,
    ).compute()
    assert value == monoid.IntPlus(sum(values))


@pytest.mark.parametrize(
    "func",
    (op.fold, op.foldr),
)
@given(st.iterables(st.integers()))
def test_IntProd_fold(func, values):
    values, values_copy = itertools.tee(values)
    value = func((monoid.IntProd(v) for v in values), monoid.IntProd)
    assert value == monoid.IntProd(
        functools.reduce(operator.mul, values_copy, monoid.IntProd.e().value),
    )


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
    "func",
    (op.fold, op.foldr),
)
@given(st.iterables(st.text()))
def test_String_fold(func, values):
    values, values_copy = itertools.tee(values)
    value = func((monoid.String(v) for v in values), monoid.String)
    assert value == monoid.String("".join(values_copy))


@st.composite
def string_chunk_size(draw, elements=st.text()):
    values = draw(st.lists(elements))
    chunk_size = draw(st.integers(min_value=1, max_value=max(len(values), 1)))
    return (values, chunk_size)


@given(string_chunk_size())
def test_String_par_fold(data):
    values, chunk_size = data
    value = parop.fold(
        (monoid.String(v) for v in values),
        monoid.String,
        chunk_size=chunk_size,
    ).compute()
    assert value == monoid.String("".join(values))
