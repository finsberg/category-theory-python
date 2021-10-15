import typing

from .core import CommutativeMonoid
from .core import Monoid


class String(Monoid[str]):
    """Monoid whose values are strings.
    Binary operation is string concatenation
    and identity element being the empty string
    """

    @staticmethod
    def e() -> "String":
        return String("")

    def __add__(self, other: "String") -> "String":
        return String(self.value + other.value)


class IntPlus(CommutativeMonoid[int]):
    """Monoid whose values are integers.
    Binary operation is the plus operation
    and identity element is 0
    """

    @staticmethod
    def e() -> "IntPlus":
        return IntPlus(0)

    def __add__(self, other: "IntPlus") -> "IntPlus":
        return IntPlus(self.value + other.value)


class IntProd(CommutativeMonoid[int]):
    """Monoid whose values are integers.
    Binary operation is the multiplication operation
    and identity element is 1
    """

    @staticmethod
    def e() -> "IntProd":
        return IntProd(1)

    def __add__(self, other: "IntProd") -> "IntProd":
        return IntProd(self.value * other.value)


class MaybeIntPlus(CommutativeMonoid[typing.Optional[int]]):
    """Monoid whose values are mayby integers.
    This means that the value can be int or None.
    Binary operation is the plus operation is the
    value is of type int and returns None otherwise.
    Identity element is MaybeIntPlus(0)
    """

    @staticmethod
    def e() -> "MaybeIntPlus":
        return MaybeIntPlus(0)

    def __add__(self, other: "MaybeIntPlus") -> "MaybeIntPlus":
        if self.value is None:
            return MaybeIntPlus(None)
        if other.value is None:
            return MaybeIntPlus(None)
        return MaybeIntPlus(self.value + other.value)


class MaybeIntProd(CommutativeMonoid[typing.Optional[int]]):
    """Monoid whose values are mayby integers.
    This means that the value can be int or None.
    Binary operation is the multiplication operation is the
    value is of type int and returns None otherwise.
    Identity element is MaybeIntProd(1)
    """

    @staticmethod
    def e() -> "MaybeIntProd":
        return MaybeIntProd(1)

    def __add__(self, other: "MaybeIntProd") -> "MaybeIntProd":
        if self.value is None:
            return MaybeIntProd(None)
        if other.value is None:
            return MaybeIntProd(None)
        return MaybeIntProd(self.value * other.value)


class Any(CommutativeMonoid[bool]):
    @staticmethod
    def e() -> "Any":
        return Any(False)

    def __add__(self, other: "Any") -> "Any":
        return Any(self.value or other.value)


class All(CommutativeMonoid[bool]):
    @staticmethod
    def e() -> "All":
        return All(True)

    def __add__(self, other: "All") -> "All":
        return All(self.value and other.value)
