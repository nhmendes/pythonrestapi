from src.domain.domaincore.gatewayinterfaces.users_gateway import UsersGateway
from src.datagateways.mongodb.user_adapter import UserAdapter


class MongoDbGateway(UsersGateway):
    def __init__(self, user_adapter: UserAdapter):
        self._user_adapter = user_adapter

    def update(self):
        self._user_adapter.to_db_model()
        print("user updated!")
