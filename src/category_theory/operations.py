import functools
import math
import typing

from .core import Monoid

a = typing.TypeVar("a")
b = typing.TypeVar("b")
c = typing.TypeVar("c")


def identity(x: a) -> a:
    r"""Identity function

    .. math::

        f : a \mapsto a \\
        f(x) = x

    Parameters
    ----------
    x : a
        Input variable

    Returns
    -------
    a
        Output variable :math:`f(x)`
    """
    return x


def is_nothing(x: typing.Optional[a]) -> typing.TypeGuard[a]:
    """Check if a variable should be declared as Nothing.

    Parameters
    ----------
    x : typing.Optional[a]
        The variable

    Returns
    -------
    typing.TypeGuard[a]
        Returns true if the variable is nothing and false otherwise.
        Note that er make use of TypGuard here which tell the type
        checker than if the thing we get in is None, then this
        function will return True
    """
    if x is None:
        return True
    if isinstance(x, float):
        return math.isinf(x) or math.isnan(x)
    return False


def compose(
    g: typing.Callable[[b], c],
    f: typing.Callable[[a], b],
) -> typing.Callable[[a], c]:
    r"""Compose two functions :math:`g` and :math:`f`, :math:`g \circ f`.

    We have the following two functions

    .. math::

        g: b \mapsto c \\
        f: a \mapsto b

    and through this function we create the composition

    .. math::

        g \circ f: a \mapsto c

    Parameters
    ----------
    g : typing.Callable[[b], c]
        Second function to be applied
    f : typing.Callable[[a], b]
        First function to be applied

    Returns
    -------
    typing.Callable[[a], c]
        The composition of `f` and `g`
    """
    return lambda x: g(f(x))


def fold(lst: typing.Iterable[Monoid], cls: typing.Type) -> typing.Any:
    """Fold an iterable of Monoids together using the identity
    element as initial.

    Parameters
    ----------
    lst : typing.Iterable[Monoid]
        An iterable of monoids that should be squashed
    cls : typing.Type
        The type of the monoid

    Returns
    -------
    typing.Any
        The reduction of the iterable.
    """

    return functools.reduce(lambda x, y: x + y, lst, cls.e())


def foldr(lst: typing.Iterable[Monoid], cls: typing.Type) -> typing.Any:
    """Same as `fold`, but from the right

    Parameters
    ----------
    lst : typing.Iterable[Monoid]
        An iterable of monoids that should be squashed
    cls : typing.Type
        The type of the monoid

    Returns
    -------
    typing.Any
        The reduction of the iterable.
    """
    return functools.reduce(lambda x, y: y + x, reversed(tuple(lst)), cls.e())
