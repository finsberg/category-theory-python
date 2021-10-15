import typing
from abc import ABC
from abc import abstractmethod

a = typing.TypeVar("a")
b = typing.TypeVar("b")


class Atomic:
    value: typing.Any

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({type(self.value)})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return False
        return self.value == other.value


class Monoid(ABC, typing.Generic[a], Atomic):
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

    @staticmethod
    @abstractmethod
    def e() -> typing.Any:
        ...

    @abstractmethod
    def __add__(self, other: typing.Any):
        ...


class CommutativeMonoid(Monoid[a]):
    """A CommutativeMonoid is just a Monoid
    where the binary operation is commutative,
    i.e :math:`a + b = b + a`
    """

    pass


class Functor(ABC, typing.Generic[a], Atomic):
    """A Functor is a mapping between categories."""

    @abstractmethod
    def map(self, func: typing.Callable[[a], b]) -> "Functor[b]":
        ...


class Applicative(Functor[a]):
    @staticmethod
    @abstractmethod
    def pure(value: a) -> "Applicative[a]":
        ...

    @abstractmethod
    def apply(self, func: "Applicative[typing.Callable[[a], b]]") -> "Applicative[b]":
        ...
