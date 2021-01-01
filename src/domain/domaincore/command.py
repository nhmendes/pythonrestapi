import abc
from typing import TypeVar, Generic


T = TypeVar('T')


class Command(Generic[T], metaclass=abc.ABCMeta):
    """
    Represents a mutable action. This action mutates
    the state of the system (create, update, delete).
    """
    @abc.abstractmethod
    def execute(self, args: T):
        pass
