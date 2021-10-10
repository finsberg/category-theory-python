import typing

from .core import Functor

a = typing.TypeVar("a")
b = typing.TypeVar("b")


class List(Functor, typing.Generic[a]):
    def __init__(self, value: typing.List[a]) -> None:
        self.value = value

    def map(self, func: typing.Callable[[a], b]) -> "List[b]":
        return List(list(map(func, self.value)))


class Maybe(Functor, typing.Generic[a]):
    def __init__(self, value: typing.Optional[a]) -> None:
        self.value = value

    def map(self, func: typing.Callable[[a], b]) -> "Maybe[b]":
        if self.value is None:
            return Maybe(None)
        return Maybe(func(self.value))
