""" User activity """

import uuid
from datetime import datetime
from dataclasses import dataclass

from activity_type import ActivityType
from operative_system import OperativeSystem


@dataclass
class UserActivity:
    """
    Represents user activity in the system.
    Eg:
    - Linux was signed out  Los Angeles, USA - Jan 3, 10:35 AM
    - New sign-in on Linux  Los Angeles, USA - Dec 31, 11:41 PM
    """

    user_id: uuid
    date_time: datetime
    country: str
    city: str
    operative_system: OperativeSystem
    activity_type: ActivityType
