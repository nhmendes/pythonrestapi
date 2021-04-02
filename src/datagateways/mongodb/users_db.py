""" mongodb gateway """

from uuid import UUID

from src.domain.domaincore.gatewayinterfaces.users_gateway import UsersGateway
from src.datagateways.mongodb.user_adapter import UserAdapter
from src.domain.domainmodel.user import User


class MongoDbGateway(UsersGateway):
    """ mongodb gateway implementation """

    def __init__(self, user_adapter: UserAdapter):
        self._user_adapter = user_adapter

    def update(self):
        """ Save the user to the mongo database """
        self._user_adapter.to_db_model()
        print("user updated!")

    def get(self, user_id: UUID) -> User:
        print(f'getting user {user_id}...')
        # return self._user_adapter.to_domain()
        return User("e6e7a9e7-e443-40ef-a42a-9e3da9cd3920", "johndoe", "John Doe", "john@doe.com")

    def delete(self, user_id: UUID):
        print(f'deleting user {user_id}...')
