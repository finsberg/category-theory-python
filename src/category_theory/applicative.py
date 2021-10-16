import typing

from . import functor
from .core import Applicative
from .operations import is_nothing

a = typing.TypeVar("a")
b = typing.TypeVar("b")


class Maybe(Applicative[a], functor.Maybe[a]):
    @staticmethod
    def pure(value: a) -> "Maybe[a]":
        return maybe(value)


class Just(Maybe, functor.Just[a]):
    def __init__(self, value: a) -> None:
        super().__init__(value)

    def apply(self, func: "Applicative[typing.Callable[[a], b]]") -> "Maybe[b]":
        if isinstance(func, _Nothing):
            return Nothing
        return maybe(func.value(self.value))


class _Nothing(Maybe, functor._Nothing[a]):
    def __init__(self, value: None = None) -> None:
        super().__init__(value)

    def apply(self, func: "Applicative[typing.Callable[[a], b]]") -> "Maybe[b]":
        return Nothing


Nothing: Maybe[typing.Any] = _Nothing()


def maybe(value: typing.Optional[a]) -> Maybe[a]:
    if is_nothing(value):
        return Nothing
    return Just(value)


class Validation(Applicative):
    pass
