import typing

from .core import Functor
from .operations import is_nothing

a = typing.TypeVar("a")
b = typing.TypeVar("b")


class List(Functor[a]):
    def __init__(self, value: typing.List[a]) -> None:
        self.value = value

    def map(self, func: typing.Callable[[a], b]) -> "List[b]":
        r"""
        Lets suppose the functor is a `List` and `a` is `int`, so that
        we have a list of integers. Then one possible :math:`f` could be

        .. math::

            f : \text{int} \mapsto \text{bool}
            f(x) = \begin{cases}
                \text{True, if } x | 2, \\
                \text{False, if } x \nmid 2.
                \end{cases}

        In other :math:`f` is the function better known as *is_even*.
        If The list is given by

        .. code::

            >> F = List([1, 2, 3, 3])

        then

        .. code::

            >> f = lambda x : x % 2 == 0
            >> F.map(f)
            List([False, True, False, True])

        Returns
        -------
        List[b]
            A new list after applying the map
        """
        return List(list(map(func, self.value)))


class Maybe(Functor[a]):
    """About maybe"""


class Just(Maybe[a]):
    def __init__(self, value: a) -> None:
        super().__init__(value)

    def map(self, func: typing.Callable[[a], b]) -> "Just[b]":
        return Just(func(self.value))


class _Nothing(Maybe[a]):
    def __init__(self, value: None = None) -> None:
        super().__init__(value)

    def map(self, func: typing.Callable[[a], b]) -> "Maybe[b]":
        return Nothing


Nothing: Maybe[typing.Any] = _Nothing()


def maybe(value: a) -> Maybe[a]:
    if is_nothing(value):
        return Nothing
    return Just(value)
