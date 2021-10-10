from category_theory import functor


def test_List():
    lst = functor.List([1, 2, 3, 4])
    is_even = lambda x: x % 2 == 0
    new_lst = lst.map(is_even)
    assert new_lst.value == [False, True, False, True]


def test_Maybe1():
    maybe = functor.Maybe(2)
    is_even = lambda x: x % 2 == 0
    new_maybe = maybe.map(is_even)
    assert new_maybe.value is True


def test_Maybe2():
    maybe = functor.Maybe(None)
    is_even = lambda x: x % 2 == 0
    new_maybe = maybe.map(is_even)
    assert new_maybe.value is None
