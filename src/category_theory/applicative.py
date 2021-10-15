import typing

from . import functor
from .core import Applicative

a = typing.TypeVar("a")
b = typing.TypeVar("b")


class Maybe(Applicative[a], functor.Maybe[a]):
    @staticmethod
    def pure(value: a) -> "Maybe[a]":
        return Maybe(value)

    # Mypy complains if we use Maby in the argument here. Why?
    def apply(self, func: "Applicative[typing.Callable[[a], b]]") -> "Maybe[b]":
        if func.value is None:
            return Maybe(None)
        if self.value is None:
            return Maybe(None)
        return Maybe(func.value(self.value))


class Validation(Applicative):
    pass
