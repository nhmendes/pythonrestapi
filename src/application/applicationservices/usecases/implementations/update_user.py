"""
Update user use case
"""

from src.domain.domaincore.gatewayinterfaces.users_gateway import UsersGateway
from src.domain.domaincore.command import Command
from src.domain.domainmodel.user import User


class UpdateUser(Command[User]):
    """
    Update user UseCase
    """

    def __init__(self, users_gateway: UsersGateway):
        self._users_gateway = users_gateway

    def execute(self, args: User):
        """
        Executes the usecase. This will replace the existing
        user with a new representation of the user.
        """
        print("update user use case")
        print(args)
        self._users_gateway.update()
