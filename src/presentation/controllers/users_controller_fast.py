from fastapi import Depends, status, APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from src.presentation.controllers.login_controller_fast import User, get_current_active_user
from src.presentation.models.jwt_token import JWTBearer


users_router = APIRouter(prefix="/users")


@users_router.get('/me', status_code=status.HTTP_200_OK)
def get_me(current_user: User = Depends(get_current_active_user), dependencies=Depends(JWTBearer())):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(current_user))


@users_router.get('/{user_id}', status_code=status.HTTP_200_OK)
async def get(user_id: str, active_user: User = Depends(get_current_active_user), dependencies=Depends(JWTBearer())):
    """
    Retrieve user details
    200 OK
    404 Not Found if user is not retrieved from the service layer (response.status_code = status.HTTP_404_NOT_FOUND)
    """

    data = {
        'user_id': user_id,
        'username': user_id,
        'name': 'nuno mendes'
    }
    
    user = User(**data)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(user))
