import typing

from .core import CommutativeMonoid
from .core import Monoid


class String(Monoid):
    def __init__(self, value: str) -> None:
        self.value = value

    @staticmethod
    def e() -> str:
        return ""

    def __add__(self, other: str) -> str:
        return self.value + other

    def __radd__(self, other: str) -> str:
        return other + self.value


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
