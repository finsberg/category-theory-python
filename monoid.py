"""
A moniod is a Set S equipped with a binary operation + : S x S -> S
such that the two following axioms holds

1) + is associative: (a + b) + c = a + (b + c)
2) There exists an identiry element e, such that a + e = e + a = a
"""
import functools
import typing
from abc import ABC
from abc import abstractmethod
from abc import abstractstaticmethod


class Monoid(ABC):
    @staticmethod
    @abstractstaticmethod
    def e():
        pass

    @abstractmethod
    def __radd__(self, other: typing.Any):
        pass

    @abstractmethod
    def __add__(self, other: typing.Any):
        pass


def squash(lst: typing.Iterable["Monoid"], cls: typing.Type):
    return functools.reduce(lambda x, y: x + y, lst, cls.e())


class CommutativeMonoid(Monoid):
    def __radd__(self, other: typing.Any) -> typing.Any:
        return self.__add__(other)


class IntPlus(CommutativeMonoid):
    def __init__(self, value: int):
        self.value = value

    @staticmethod
    def e():
        return 0

    def __add__(self, other: int) -> int:
        return self.value + other


class IntProd(CommutativeMonoid):
    def __init__(self, value: int):
        self.value = value

    @staticmethod
    def e():
        return 1

    def __add__(self, other: int) -> int:
        return self.value * other
