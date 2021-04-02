import unittest
from unittest.mock import Mock

from uuid import UUID
from src.domain.domaincore.gatewayinterfaces.users_gateway import UsersGateway
from src.domain.domainmodel.user import User
from src.domain.domainmodel.email import Email
from src.application.applicationservices.usecases.implementations.get_user import GetUserById


class TestGetUserById(unittest.TestCase):

    def test_get_existing_user(self):
        # Arrange
        user_id: UUID = UUID('eac9bea1-46c7-4434-8c78-3f7d5de1e8d2')
        expected = User(
            user_id,
            'username',
            'name',
            Email('myemail@test.com'))

        mock_gateway = Mock(UsersGateway)
        mock_gateway.get = Mock(return_value=expected)

        # Act
        get_user_usecase = GetUserById(mock_gateway)
        actual = get_user_usecase.execute(expected.user_id)

        # Assert
        mock_gateway.get.assert_called_with(expected.user_id)

        self.assertIsNotNone(actual)
        self.assertEqual(expected, actual)

    def test_get_non_existing_user(self):
        user_id: UUID = UUID('eac9bea1-46c7-4434-8c78-3f7d5de1e8d2')

        mock_gateway = Mock(UsersGateway)
        mock_gateway.get = Mock(return_value=None)

        get_user_usecase = GetUserById(mock_gateway)
        actual = get_user_usecase.execute(user_id)

        mock_gateway.get.assert_called_with(user_id)

        self.assertIsNone(actual)
