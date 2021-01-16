"""
Delete user use case
"""

from uuid import UUID
from src.domain.domaincore.gatewayinterfaces.users_gateway import UsersGateway
from src.domain.domaincore.command import Command
from src.domain.domainmodel.user import User


class DeleteUser(Command[UUID, None]): # pylint: disable=too-few-public-methods
    """
    Delete user UseCase
    """

    def __init__(self, users_gateway: UsersGateway):
        self._users_gateway = users_gateway

    def execute(self, arg: UUID) -> None:
        """
        Executes the usecase. This will disable the user (soft delete).
        After the user is disabled it will no longer be returned.
        """
        print("Delete user use case")
        print(arg)
        self._users_gateway.delete(arg)
