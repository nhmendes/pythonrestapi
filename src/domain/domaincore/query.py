import abc
from typing import TypeVar, Generic


T = TypeVar('T')
U = TypeVar('U')


class Query(Generic[T, U], metaclass=abc.ABCMeta):
    def execute(self, args: T) -> U:
        pass
