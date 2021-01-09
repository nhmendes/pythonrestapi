from pydantic import BaseModel
from typing import Optional
from datetime import timedelta
from jose import JWTError, jwt

from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.config.config import Settings
from src.presentation.models.token import Token
from src.presentation.models.user import User
from src.presentation.models.jwt_token import create_access_token


config = Settings()
SECRET_KEY = config.jwt_secret_key
ALGORITHM = config.jwt_algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = config.jwt_access_token_expires


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
token_router = APIRouter(prefix="/token")


class TokenData(BaseModel):
    username: Optional[str] = None


def get_user(username: str):
    return {
        'user_id': username,
        'username': username,
        'name': 'nuno mendes',
        'email': 'aaaa@aaaa.com',
        'disabled': False
    }


def authenticate_user(username: str, password: str):
    data = {
        'user_id': username,
        'username': username,
        'email': 'aaaa@aaaa.com',
        'name': 'nuno mendes'
    }
    return User(**data)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user['disabled']:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    return current_user


@token_router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
