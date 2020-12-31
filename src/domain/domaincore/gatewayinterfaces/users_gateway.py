from abc import ABC, abstractmethod

class UsersGateway(ABC):
    @abstractmethod
    def update(self):
        raise NotImplementedError
