import typing
from abc import ABC
from abc import abstractmethod

a = typing.TypeVar("a")
b = typing.TypeVar("b")


class Monoid(ABC):
    """
    A moniod is a Set S equipped with a binary
    operation + : S x S -> S such that the two
    following axioms holds:

    - :math:`x` is associative: :math:`(a + b) + c = a + (b + c)`

    - There exists an identity element :math:`e`,
      such that `a + e = e + a = a`

    In this interface the binary operation used is `+`, so that
    any class that wants inherit from `Monoid` need to implement
    `__add__` and `__radd__`. For the identity element we require
    a `staticmethod` called `e`.

    """

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


class CommutativeMonoid(Monoid):
    """A CommutativeMonoid is just a Monoid
    where the binary operation is commutative,
    i.e :math:`a + b = b + a`
    """

    def __radd__(self, other: typing.Any) -> typing.Any:
        return self.__add__(other)


class Functor(ABC, typing.Generic[a]):
    @abstractmethod
    def map(self, func: typing.Callable[[a], b]) -> "Functor[b]":
        ...
