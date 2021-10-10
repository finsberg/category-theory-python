import functools
import typing
from itertools import zip_longest

import dask

from .core import Monoid


def chunkify(
    chunk_size: int,
    iterable: typing.Iterable[typing.Any],
    fillvalue: typing.Any = None,
) -> typing.Iterable[typing.Iterable[typing.Any]]:
    """Split iterable into chunks of size `chunk_size`.
    If all chunks does not add up, it will use the
    `fillvalue` in the remainin spots

    Parameters
    ----------
    chunk_size : int
        Number of elements in each chunk
    iterable : typing.Iterable[typing.Any]
        The iterable that should be chunkified
    fillvalue : typing.Any, optional
        A value to put in those places when the
        chunk size does not add up, by default None

    Returns
    -------
    typing.Iterable[typing.Iterable[typing.Any]]
        A list of new iterables, each being of size `chunk_size`.

    Example
    -------

    .. code:: python

        >> iterable = (1, 2, 3, 4, 5)
        >> chunkify(3, iterable, fillvalue=None)
        ((1, 2, 3), (4, 5, None))

    """
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
