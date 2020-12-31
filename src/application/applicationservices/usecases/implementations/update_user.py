from src.domain.domaincore.gatewayinterfaces.users_gateway import UsersGateway


class UpdateUser:
    def __init__(self, users_gateway: UsersGateway):
        self._usersGateway = users_gateway

    def update(self):
        print("update user use case")
        self._usersGateway.update()
