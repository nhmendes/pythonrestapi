from uuid import UUID
from src.domain.domaincore.gatewayinterfaces.users_gateway import UsersGateway
from src.domain.domaincore.command import Command
from src.domain.domainmodel.user import User


class GetUserById(Command[UUID, User]):
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

        # TODO: add application business logic here

        result = self._users_gateway.get(arg)

        # TODO: add application business logic here

        return result
