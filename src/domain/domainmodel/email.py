""" Email """

import re
from dataclasses import dataclass

from src.domain.domainmodel.exceptions.invalid_email import InvalidEmail


@dataclass
class Email:
    """ This class represents the Email datatype """

    value: str

    """ Email value object """

    def __init__(self, value: str):
        if self._validate_email(value) is False:
            raise InvalidEmail()
        self.value = value

    @classmethod
    def _validate_email(cls, value: str):
        pattern = r"^[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}$"
        return bool(re.match(pattern, value))
