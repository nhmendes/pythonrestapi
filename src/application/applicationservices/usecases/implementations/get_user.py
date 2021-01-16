"""
Get user by user_id
"""
from uuid import UUID
from src.domain.domaincore.gatewayinterfaces.users_gateway import UsersGateway
from src.domain.domaincore.command import Command
from src.domain.domainmodel.user import User


class GetUserById(Command[UUID, User]): # pylint: disable=too-few-public-methods
    """
    Get user by id UseCase
    """

    def __init__(self, users_gateway: UsersGateway):
        self._users_gateway = users_gateway

    def execute(self, arg: UUID) -> User:
        """
        Executes the usecase. This will return a user by id.
        """
        print("get user by id use case")
        print(arg)
        return self._users_gateway.get(arg)
