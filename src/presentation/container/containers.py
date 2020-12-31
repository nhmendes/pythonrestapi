from dependency_injector import providers, containers

from src.domain.domaincore.gatewayinterfaces.users_gateway import UsersGateway
from src.application.applicationservices.usecases.implementations.update_user import UpdateUser
from src.datagateways.mongodb.users_db import MongoDbGateway
from src.datagateways.mongodb.user_adapter import UserAdapter


class Container(containers.DeclarativeContainer):

    # Configuration
    config = providers.Configuration()

    # Gateways
    user_adapter = providers.Singleton(UserAdapter)
    users_gateway = providers.Factory(
        MongoDbGateway, 
        user_adapter=user_adapter)

    # Use cases
    update_user = providers.Factory(
        UpdateUser, 
        users_gateway=users_gateway)


container = Container()
container.config.from_yaml('src/presentation/config/config.yaml')
