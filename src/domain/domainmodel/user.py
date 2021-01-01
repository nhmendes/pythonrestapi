import uuid
from dataclasses import dataclass

from src.domain.domainmodel.email import Email


@dataclass
class User:
    user_id: uuid
    username: str
    email: Email
