import functools
import typing

from .core import Monoid


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
