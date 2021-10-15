from category_theory import applicative


def test_maybe_just_just():
    maybe = applicative.Maybe.pure(3)
    func = applicative.Maybe.pure(lambda x: x + 1)
    new_maybe = maybe.apply(func)
    assert new_maybe == applicative.Maybe(4)


def test_maybe_just_nothing():
    maybe = applicative.Maybe.pure(3)
    func = applicative.Maybe.pure(None)
    new_maybe = maybe.apply(func)
    assert new_maybe == applicative.Maybe(None)


def test_maybe_nothing_just():
    maybe = applicative.Maybe.pure(None)
    func = applicative.Maybe.pure(lambda x: x + 1)
    new_maybe = maybe.apply(func)
    assert new_maybe == applicative.Maybe(None)
