from abc import ABC, abstractmethod


class UserState(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    def invited(self):
        raise Exception("Invalid operation")

    def active(self):
        raise Exception("Invalid operation")

    def disabled(self):
        raise Exception("Invalid operation")

    def deleted(self):
        raise Exception("Invalid operation")
