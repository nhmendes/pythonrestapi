""" Operative system """

from enum import Enum


class OperativeSystem(Enum):
    """ represents the operative systems """

    LINUX = "Linux"
    MAC = "Mac"
    WINDOWS = "Windows"
    UNIDENTIFIED: "Unindentified"
