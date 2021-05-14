from enum import Enum


class UserStatus(Enum):
    Invited = "invited"
    Active = "active"
    Disabled = "disabled"
    Deleted = "deleted"
