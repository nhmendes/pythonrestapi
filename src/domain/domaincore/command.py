""" Generic command """

import abc
from typing import TypeVar, Generic


TInput = TypeVar('TInput')
TOutput = TypeVar('TOutput')


class Command(Generic[TInput, TOutput], metaclass=abc.ABCMeta): # pylint: disable=too-few-public-methods
    """
    Represents a mutable action. This action mutates
    the state of the system (create, update, delete).
    """

    @abc.abstractmethod
    def execute(self, args: TInput) -> TOutput:
        """
        Execute method for the command.
        This method should be implemented by the child class.
        """
