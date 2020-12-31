from flask import Flask
from flask_jwt_extended import JWTManager

from src.presentation.container.containers import Container
from src.presentation.controllers.users_controller import users_api
from src.presentation.controllers.login_controller import login_api


ENV_FILE_LOCATION='src/config/.env'


container = Container()
container.config.from_yaml('src/presentation/config/config.yaml')


app = Flask(__name__)
app.url_map.strict_slashes = False
# app.container = container


# setup JWT
jwt = JWTManager(app)
# app.config.from_envvar(ENV_FILE_LOCATION)
app.config.from_pyfile(ENV_FILE_LOCATION)


# Setup Login API
login_api_version = '/'
login_url_prefix = f'/login{login_api_version}'
app.register_blueprint(login_api, url_prefix=login_url_prefix)


# Setup Users API
users_api_version = '/'
users_url_prefix = f'/users{users_api_version}'
app.register_blueprint(users_api, url_prefix=users_url_prefix)


if __name__ == "__main__":
    app.run(debug=True)
