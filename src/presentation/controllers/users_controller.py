import json
import uuid
from http import HTTPStatus
from dataclasses import dataclass
from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required

from src.presentation.container.containers import container
from src.presentation.controllers.error import ApiError
from src.domain.domainmodel.user import User
from src.domain.domainmodel.email import Email
from src.domain.domainmodel.exceptions.invalid_email import InvalidEmail


# blueprints
users_api = Blueprint('users_api', __name__)


# use cases
update_user = container.update_user()


@dataclass
class UpdateUserRequest:
    user_id: uuid
    username: str
    email: str

    def to_domain(self):
        return User(self.user_id, self.username, Email(self.email))


@users_api.errorhandler(ApiError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response



@users_api.route('/', methods=['GET'])
@jwt_required
def query():
    """
    Retrieve details of users with a search criteria.
    Supported search criteria:
    - Name
    """
    name = request.args.get('name')
    return jsonify(name), HTTPStatus.OK


@users_api.route('/<int:user_id>', methods=['GET'])
@jwt_required
def get(user_id: int):
    """ Retrieve user details """

    user = {
        'id': user_id,
        'name': 'nuno mendes'
    }

    return jsonify(user), HTTPStatus.OK


@users_api.route('/', methods=['POST'])
@jwt_required
def post():
    """ Create a new user """
    record = json.loads(request.data)
    print(record)

    new_record = {
        'id': 123,
        'name': record['name']
    }

    return jsonify(), HTTPStatus.CREATED, {'location': f'/users/{new_record["id"]}'}


@users_api.route('/<int:user_id>', methods=['DELETE'])
@jwt_required
def delete(user_id: int):
    """
    Deletes a user
    if user is not found, returns a 404 NOT_FOUND http status code
    """
    print(user_id)
    print("deleted")
    return jsonify(), HTTPStatus.NO_CONTENT


@users_api.route('/<int:user_id>', methods=['PUT'])
@jwt_required
def put(user_id: int):
    """ Replaces the stored representation of the User with the request User """

    try:
        record = json.loads(request.data)
        update_request = UpdateUserRequest(record["user_id"], record["username"], record["email"])
        update_user.execute(update_request.to_domain())
    except KeyError as error:
        raise ApiError("invalid property", HTTPStatus.BAD_REQUEST) from error
    except InvalidEmail as error:
        raise ApiError(error.message, HTTPStatus.BAD_REQUEST) from error
    except Exception as error: # pylint: disable=broad-except
        raise ApiError("an error occured", HTTPStatus.INTERNAL_SERVER_ERROR) from error
    else:
        return jsonify(), HTTPStatus.NO_CONTENT, {'location': f'/users/{user_id}'}


@users_api.route('/<int:user_id>/roles', methods=['POST'])
@jwt_required
def post_role(user_id: int):
    """ Assign a role to a user """
    record = json.loads(request.data)
    print(record)

    new_record = {
        'user_id': user_id,
        'role_id': record.role_id
    }

    return jsonify(), HTTPStatus.CREATED, {'location': f'/users/{new_record["role_id"]}'}


@users_api.route('/<int:user_id>/roles', methods=['GET'])
@jwt_required
def get_role(user_id: int):
    """ Get all roles for a given user """

    roles = [{
        'id': 'role_id_1',
        'name': 'role #1'
    }, {
        'id': 'role_id_1',
        'name': 'role #2'
    }]

    return jsonify(roles), HTTPStatus.OK


@users_api.route('/<int:user_id>/roles/<string:role_id>', methods=['DELETE'])
@jwt_required
def delete_role(user_id: int, role_id: str):
    """ Removes a role from a user """
    return jsonify(), HTTPStatus.NO_CONTENT
