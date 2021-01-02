""" User """

import uuid
from dataclasses import dataclass

from src.domain.domainmodel.email import Email


@dataclass
class User:
    """ Represents a domain User """

    user_id: uuid
    username: str
    email: Email
