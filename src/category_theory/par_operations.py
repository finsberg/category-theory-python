import functools
import typing
from itertools import zip_longest

import dask

from .core import Monoid


def chunkify(chunk_size, iterable, fillvalue=None):

    args = [iter(iterable)] * chunk_size
    return zip_longest(fillvalue=fillvalue, *args)


def fold(
    iterable: typing.Iterable[Monoid],
    cls: typing.Type,
    chunk_size=1000,
) -> typing.Any:
    """Fold an iterable of Monoids together using the identity
    element as initial.

    Parameters
    ----------
    iterable : typing.Iterable[Monoid]
        An iterable of monoids that should be squashed
    cls : typing.Type
        The type of the monoid

    Returns
    -------
    typing.Any
        The reduction of the iterable.
    """
    output = []
    for chunk in chunkify(chunk_size, iterable, fillvalue=cls.e()):
        future = dask.delayed(functools.reduce)(lambda x, y: x + y, chunk, cls.e())
        output.append(future)

    return dask.delayed(functools.reduce)(lambda x, y: x + y, output, cls.e())
