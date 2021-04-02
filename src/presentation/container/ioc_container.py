""" IoC Container """

from src.presentation.typeadapters.user_type_adapter import UserTypeAdapter
from dependency_injector import providers, containers

from src.application.applicationservices.usecases.implementations.update_user import UpdateUser
from src.application.applicationservices.usecases.implementations.delete_user import DeleteUser
from src.application.applicationservices.usecases.implementations.get_user import GetUserById
from src.datagateways.mongodb.users_db import MongoDbGateway
from src.datagateways.mongodb.user_adapter import UserAdapter


class Container(containers.DeclarativeContainer):
    """ IoC Container """

    # Configuration
    config = providers.Configuration()

    # Type adapters
    repo_user_adapter = providers.Singleton(UserAdapter)
    controller_user_adapter = providers.Singleton(UserTypeAdapter)

    # Gateways
    users_gateway = providers.Factory(
        MongoDbGateway,
        user_adapter=repo_user_adapter)

    # Use cases
    update_user = providers.Factory(
        UpdateUser,
        users_gateway=users_gateway)

    delete_user = providers.Factory(
        DeleteUser,
        users_gateway=users_gateway)

    get_user_by_id = providers.Factory(
        GetUserById,
        users_gateway=users_gateway)


container = Container()
container.config.from_yaml('src/presentation/config/config.yaml')
