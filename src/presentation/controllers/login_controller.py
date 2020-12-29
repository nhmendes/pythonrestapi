from flask import request, jsonify, Blueprint
from http import HTTPStatus
from flask_jwt_extended import (
    jwt_required,
    create_access_token
)


login_api = Blueprint('login_api', __name__)


@login_api.route('/', methods=['POST'])
def login():
    """
    Retrieve details of users with a search criteria.
    Supported search criteria:
    - Name
    """
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if username != 'test' or password != 'test':
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), HTTPStatus.OK
