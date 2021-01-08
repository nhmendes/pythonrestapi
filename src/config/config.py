from pydantic import BaseSettings


class Settings(BaseSettings):
    jwt_secret_key: str
    jwt_access_token_expires: int
    jwt_algorithm: str

    class Config:
        env_file = "src/config/.env"
