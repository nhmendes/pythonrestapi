""" generic query """

import abc
from typing import TypeVar, Generic


TInput = TypeVar('TInput')
TOutput = TypeVar('TOutput')


class Query(Generic[TInput, TOutput], metaclass=abc.ABCMeta): # pylint: disable=too-few-public-methods
    """
    Represents a readonly action. This action DOES NOT mutate
    the state of the system (get, query).
    """

    def execute(self, arg: TInput) -> TOutput:
        """
        Execute method for the query.
        This method should be implemented by the child class.
        """
