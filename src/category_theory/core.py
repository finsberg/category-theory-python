import typing
from abc import ABC
from abc import abstractmethod
from abc import abstractstaticmethod


class Monoid(ABC):
    @staticmethod
    @abstractstaticmethod
    def e():
        ...

    @abstractmethod
    def __radd__(self, other: typing.Any):
        ...

    @abstractmethod
    def __add__(self, other: typing.Any):
        ...


class CommutativeMonoid(Monoid):
    def __radd__(self, other: typing.Any) -> typing.Any:
        return self.__add__(other)
