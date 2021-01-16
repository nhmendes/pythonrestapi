from uuid import UUID
from fastapi import Depends, status, APIRouter
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder

from src.presentation.controllers.login_controller_fast import User, get_current_active_user
from src.presentation.models.jwt_token import JWTBearer
from src.presentation.container.ioc_container import container
from src.presentation.controllers.api_error import ApiError
from src.domain.domainmodel.exceptions.invalid_email import InvalidEmail
from src.domain.domainmodel.user import User as DomainUser


users_router = APIRouter(prefix="/users")

# use cases
update_user_usecase = container.update_user()
delete_user_usecase = container.delete_user()
get_user_by_id_usecase = container.get_user_by_id()


class UserTypeAdapter:
    @staticmethod
    def from_domain(domain_user: DomainUser):
        return User()

    def to_domain(user: User):
        return DomainUser()


@users_router.get('/me', status_code=status.HTTP_200_OK)
def get_logged_user(active_user: User = Depends(get_current_active_user), dependencies=Depends(JWTBearer())):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(active_user))


@users_router.get('/{user_id}', status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: UUID, dependencies=Depends(JWTBearer())):
    """
    Retrieve user details
    200 OK
    404 Not Found if user is not retrieved from the service layer (response.status_code = status.HTTP_404_NOT_FOUND)
    """

    domain_user = get_user_by_id_usecase.execute(user_id)

    user = UserTypeAdapter.from_domain(domain_user=domain_user)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(user))


@users_router.post('/')
def create_new_user(user: User, dependencies=Depends(JWTBearer())):
    """ Create a new user """

    new_record = user

    location = users_router.url_path_for('get_user_by_id', user_id=new_record.user_id)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(new_record),
        headers={'location': location})


@users_router.put('/')
def update_user(user: User, dependencies=Depends(JWTBearer())):
    """ Replaces the stored representation of the User with the request User """
    try:
        update_user_usecase.execute(user.to_domain())
    except KeyError as error:
        raise ApiError("invalid property", status.HTTP_400_BAD_REQUEST) from error
    except InvalidEmail as error:
        raise ApiError(error.message, status.HTTP_400_BAD_REQUEST) from error
    except Exception as error: # pylint: disable=broad-except
        raise ApiError("an error occured", status.HTTP_500_INTERNAL_SERVER_ERROR) from error
    else:
        return Response(
            status_code=status.HTTP_204_NO_CONTENT,
            headers={'location': users_router.url_path_for('get_user_by_id', user_id=user.user_id)})


@users_router.delete('/<string:user_id>')
def delete(user_id: str):
    """
    Deletes a user
    if user is not found, returns a 404 NOT_FOUND http status code
    """
    delete_user_usecase.execute(user_id)
    return Response(
            status_code=status.HTTP_204_NO_CONTENT)
