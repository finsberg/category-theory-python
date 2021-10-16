import typing

from .core import Functor
from .operations import is_nothing

a = typing.TypeVar("a")
b = typing.TypeVar("b")


class List(Functor[a]):
    def __init__(self, value: typing.List[a]) -> None:
        self.value = value

    def map(self, func: typing.Callable[[a], b]) -> "List[b]":
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
