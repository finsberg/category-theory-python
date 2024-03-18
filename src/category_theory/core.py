import typing
from abc import ABC
from abc import abstractmethod

a = typing.TypeVar("a")
b = typing.TypeVar("b")


class Atomic:
    def __init__(self, value: typing.Any) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({type(self.value)})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return False
        return self.value == other.value


class Monoid(ABC, typing.Generic[a], Atomic):
    r"""
    A monoid is a type :math:`a` equipped with a binary
    operation :math:`+ : a \times a \rightarrow a` such that the two
    following axioms holds:

    - :math:`x` is associative: :math:`(a + b) + c = a + (b + c)`

    - There exists an identity element :math:`e`,
      such that `a + e = e + a = a`

    In this interface the binary operation used is `+`, so that
    any class that wants inherit from `Monoid` need to implement
    `__add__` and `__radd__`. For the identity element we require
    a `staticmethod` called `e`.

    A key features of the Monoid structure which separates it from a
    semigroup is the presence of an identity element.
    """

    def __init__(self, value: a) -> None:
        self.value = value  # pragma: no cover

    @staticmethod
    @abstractmethod
    def e() -> typing.Any:
        """Identity element"""
        ...

    @abstractmethod
    def __add__(self, other: typing.Any):
        """Binary operation"""
        ...


class CommutativeMonoid(Monoid[a]):
    """A CommutativeMonoid is just a Monoid
    where the binary operation is commutative,
    i.e :math:`a + b = b + a`
    """

    pass


class Functor(ABC, typing.Generic[a], Atomic):
    """A Functor is a mapping between categories.

    In programming sense we typically think of a Functor
    as a container, parameterized by a type `a`.

    Examples for Functors are Lists and Queues
    which are structures that we typically would think of as
    containers, but other examples of Functors are
    Maybe, Either and Promise which are less container like.
    The key features is that the structure contains something, and
    given a function, we can apply it to the thing inside our structure.
    Note that the thing inside the structure has type `a`.

    Example
    -------
    For example `a` could be string and the functor could
    be `List`, in which case we have a list of strings.
    """

    @abstractmethod
    def map(self, func: typing.Callable[[a], b]) -> "Functor[b]":
        r"""Take a function and apply it to each element in the structure

        Given a function

        .. math::

            f : a \mapsto b

        apply :math:`f` to all elements in the structure.

        """
        ...


class Applicative(Functor[a]):
    """An applicative functor is a functor that

    Parameters
    ----------
    Functor : [type]
        [description]
    """

    @staticmethod
    @abstractmethod
    def pure(value: a) -> "Applicative[a]": ...

    @abstractmethod
    def apply(
        self, func: "Applicative[typing.Callable[[a], b]]",
    ) -> "Applicative[b]": ...
