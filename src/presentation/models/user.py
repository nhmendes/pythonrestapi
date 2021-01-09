from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    user_id: str
    username: str
    name: str
    active: Optional[bool] = True
