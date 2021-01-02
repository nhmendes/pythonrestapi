""" User """

import uuid
from dataclasses import dataclass


@dataclass
class User():
    """ Represents a database user data type """
    user_id: uuid
    username: str
    email: str
