from flask import Flask
from flask_jwt_extended import JWTManager

from src.presentation.container.ioc_container import Container
from src.presentation.controllers.users_controller import users_api
from src.presentation.controllers.login_controller import login_api


ENV_FILE_LOCATION = 'src/config/.env'


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
LOGIN_API_VERSION = '/'
login_url_prefix = f'/login{LOGIN_API_VERSION}'
app.register_blueprint(login_api, url_prefix=login_url_prefix)


# Setup Users API
USERS_API_VERSION = '/'
users_url_prefix = f'/users{USERS_API_VERSION}'
app.register_blueprint(users_api, url_prefix=users_url_prefix)


if __name__ == "__main__":
    app.run(debug=True)
