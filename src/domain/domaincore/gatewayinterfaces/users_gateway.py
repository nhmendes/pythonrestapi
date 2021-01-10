""" gateway interface """

import uuid
from abc import ABC, abstractmethod


class UsersGateway(ABC): # pylint: disable=too-few-public-methods
    """ Data gateway interface """

    @abstractmethod
    def update(self):
        """ abstract methods to be implemented by the child class """
        raise NotImplementedError

    @abstractmethod
    def get(self, user_id: uuid):
        """ method to get a user """
        raise NotImplementedError

    @abstractmethod
    def delete(self, user_id: uuid):
        """ method to get a user """
        raise NotImplementedError
