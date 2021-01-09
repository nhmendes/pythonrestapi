from pydantic import BaseModel
from typing import Optional

from src.domain.domainmodel.email import Email
from src.domain.domainmodel.user import User as DomainUser 


class User(BaseModel):
    user_id: str
    username: str
    name: str
    email: str
    active: Optional[bool] = True

    def to_domain(self) -> DomainUser:
        """ Converts from UpdateUserRequest to the domain User datatype """
        return DomainUser(user_id=self.user_id, username=self.username, name=self.name, email=Email(self.email))
