import typing
from abc import ABC
from abc import abstractmethod

a = typing.TypeVar("a")
b = typing.TypeVar("b")


class Monoid(ABC, typing.Generic[a]):
    r"""
    A moniod is a type :math:`a` equipped with a binary
    operation :math:`+ : a \times a \rightarrow a` such that the two
    following axioms holds:

    - :math:`x` is associative: :math:`(a + b) + c = a + (b + c)`

    - There exists an identity element :math:`e`,
      such that `a + e = e + a = a`

    In this interface the binary operation used is `+`, so that
    any class that wants inherit from `Monoid` need to implement
    `__add__` and `__radd__`. For the identity element we require
    a `staticmethod` called `e`.

    """

    def __init__(self, value: a) -> None:
        self.value = value  # pragma: no cover

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Monoid):
            raise NotImplementedError
        return self.value == other.value

    @staticmethod
    @abstractmethod
    def e() -> typing.Any:
        ...

    @abstractmethod
    def __radd__(self, other: typing.Any):
        ...

    @abstractmethod
    def __add__(self, other: typing.Any):
        ...


class CommutativeMonoid(Monoid[a]):
    """A CommutativeMonoid is just a Monoid
    where the binary operation is commutative,
    i.e :math:`a + b = b + a`
    """

    def __radd__(self, other: typing.Any) -> typing.Any:
        return self.__add__(other)


class Functor(ABC, typing.Generic[a]):
    """A Functor is a mapping between categories."""

    @abstractmethod
    def map(self, func: typing.Callable[[a], b]) -> "Functor[b]":
        ...
