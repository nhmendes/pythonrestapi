""" Activity type """

from enum import Enum


class ActivityType(Enum):
    """ represents the types of activities a user can perform in the system """

    SIGN_IN = "sign-in"
    SIGN_OUT = "sign-out"
