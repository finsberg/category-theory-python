import typing

from category_theory import functor
from category_theory.operations import compose
from category_theory.operations import identity
from hypothesis import given
from hypothesis import strategies as st

a = typing.Union[str, int, float, bool]
b = typing.Union[str, int, float, bool]

monoids = (st.integers(), st.booleans(), st.characters(), st.floats(allow_nan=False))

all_lists = st.lists(st.one_of(*monoids))


def test_List():
    lst = functor.List([1, 2, 3, 4])
    is_even = lambda x: x % 2 == 0
    new_lst = lst.map(is_even)
    assert new_lst.value == [False, True, False, True]


@given(all_lists)
def test_List_identity(x):
    lst = functor.List(x)
    assert identity(lst) == lst.map(identity)


@st.composite
def chained_functions(draw, elements=st.integers()):
    def f(x: int) -> float:  # type: ignore
        ...

    def g(y: float) -> str:  # type: ignore
        ...

    func1 = draw(st.functions(like=f, pure=True, returns=st.floats()))
    func2 = draw(st.functions(like=g, pure=True, returns=st.characters()))
    return (func1, func2)


@given(chained_functions(), st.lists(st.integers()))
def test_List_composition(fg, x):
    f, g = fg
    lst = functor.List(x)
    assert lst.map(f).map(g) == lst.map(compose(g, f))


@given(st.one_of(*monoids))
def test_Maybe_identity(x):
    maybe = functor.maybe(x)
    assert identity(maybe) == maybe.map(identity)


@given(chained_functions(), st.one_of(st.integers(), st.none()))
def test_Maybe_composition(fg, x):
    f, g = fg
    maybe = functor.maybe(x)
    lhs = maybe.map(f).map(g)
    rhs = maybe.map(compose(g, f))
    assert lhs == rhs, f"lhs = {lhs.value}, rhs = {rhs.value}"


def test_Maybe_int_just():
    maybe = functor.maybe(2)
    is_even = lambda x: x % 2 == 0
    new_maybe = maybe.map(is_even)
    assert new_maybe == functor.maybe(True)


def test_Maybe_int_Nothing():
    maybe = functor.maybe(None)
    is_even = lambda x: x % 2 == 0
    new_maybe = maybe.map(is_even)
    assert new_maybe == functor.Nothing


def test_Maybe_repr():
    assert repr(functor.maybe(1)) == "Just(<class 'int'>)"


def test_Maybe_comparison_with_different_types():
    assert functor.maybe(1) != functor.maybe("1")


def test_comparison_with_different_types():
    assert functor.maybe(1) != functor.List([1])
