import typing

from .core import CommutativeMonoid
from .core import Monoid


class String(Monoid):
    """Monoid whose values are strings.
    Binary operation is string concatenation
    and identity element being the empty string
    """

    def __init__(self, value: str) -> None:
        self.value = value

    @staticmethod
    def e() -> "String":
        return String("")

    def __add__(self, other: "String") -> "String":
        return String(self.value + other.value)

    def __radd__(self, other: "String") -> "String":
        return String(other.value + self.value)


class IntPlus(CommutativeMonoid):
    """Monoid whose values are integers.
    Binary operation is the plus operation
    and identity element is 0
    """

    def __init__(self, value: int) -> None:
        self.value = value

    @staticmethod
    def e() -> "IntPlus":
        return IntPlus(0)

    def __add__(self, other: "IntPlus") -> "IntPlus":
        return IntPlus(self.value + other.value)


class IntProd(CommutativeMonoid):
    """Monoid whose values are integers.
    Binary operation is the multiplication operation
    and identity element is 1
    """

    def __init__(self, value: int) -> None:
        self.value = value

    @staticmethod
    def e() -> "IntProd":
        return IntProd(1)

    def __add__(self, other: "IntProd") -> "IntProd":
        return IntProd(self.value * other.value)


class MaybeIntPlus(CommutativeMonoid):
    """Monoid whose values are mayby integers.
    This means that the value can be int or None.
    Binary operation is the plus operation is the
    value is of type int and returns None otherwise.
    Identity element is MaybeIntPlus(0)
    """

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
