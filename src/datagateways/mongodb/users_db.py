""" mongodb gateway """

from uuid import UUID

from src.domain.domaincore.gatewayinterfaces.users_gateway import UsersGateway
from src.datagateways.mongodb.user_adapter import UserAdapter
from src.domain.domainmodel.user import User


class MongoDbGateway(UsersGateway): # pylint: disable=too-few-public-methods
    """ mongodb gateway implementation """

    def __init__(self, user_adapter: UserAdapter):
        self._user_adapter = user_adapter

    def update(self):
        """ Save the user to the mongo database """
        self._user_adapter.to_db_model()
        print("user updated!")

    def get(self, user_id: UUID) -> User:
        print(f'getting user {user_id}...')
        return self._user_adapter.to_domain()

    def delete(self, user_id: UUID):
        print(f'deleting user {user_id}...')
