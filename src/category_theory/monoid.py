"""
A moniod is a Set S equipped with a binary operation + : S x S -> S
such that the two following axioms holds

1) + is associative: (a + b) + c = a + (b + c)
2) There exists an identiry element e, such that a + e = e + a = a
"""
import functools
import typing

from .core import CommutativeMonoid
from .core import Monoid


def squash(lst: typing.Iterable["Monoid"], cls: typing.Type):
    return functools.reduce(lambda x, y: x + y, lst, cls.e())


class IntPlus(CommutativeMonoid):
    def __init__(self, value: int) -> None:
        self.value = value

    @staticmethod
    def e() -> int:
        return 0

    def __add__(self, other: int) -> int:
        return self.value + other


class IntProd(CommutativeMonoid):
    def __init__(self, value: int) -> None:
        self.value = value

    @staticmethod
    def e() -> int:
        return 1

    def __add__(self, other: int) -> int:
        return self.value * other


class MaybeIntPlus(CommutativeMonoid):
    def __init__(self, value: typing.Optional[int]):
        self.value = value

    @staticmethod
    def e() -> "MaybeIntPlus":
        return MaybeIntPlus(0)

    def __add__(self, other: "MaybeIntPlus") -> "MaybeIntPlus":
        if self.value is None:
            return MaybeIntPlus(None)
        if other.value is None:
            return MaybeIntPlus(None)
        return MaybeIntPlus(self.value + other.value)
