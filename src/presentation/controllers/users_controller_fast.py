from fastapi import Depends, status, APIRouter
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder

from src.presentation.controllers.login_controller_fast import User, get_current_active_user
from src.presentation.models.jwt_token import JWTBearer
from src.presentation.container.ioc_container import container
from src.presentation.controllers.api_error import ApiError
from src.domain.domainmodel.exceptions.invalid_email import InvalidEmail


users_router = APIRouter(prefix="/users")

# use cases
update_user_usecase = container.update_user()


@users_router.get('/me', status_code=status.HTTP_200_OK)
def get_logged_user(active_user: User = Depends(get_current_active_user), dependencies=Depends(JWTBearer())):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(active_user))


@users_router.get('/{user_id}', status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: str, dependencies=Depends(JWTBearer())):
    """
    Retrieve user details
    200 OK
    404 Not Found if user is not retrieved from the service layer (response.status_code = status.HTTP_404_NOT_FOUND)
    """
    
    user = User(user_id=user_id, username='username', name='name', email='email')

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
