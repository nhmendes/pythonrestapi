""" gateway interface """

from abc import ABC, abstractmethod


class UsersGateway(ABC): # pylint: disable=too-few-public-methods
    """ Data gateway interface """

    @abstractmethod
    def update(self):
        """ abstract methods to be implemented by the child class """
        raise NotImplementedError
