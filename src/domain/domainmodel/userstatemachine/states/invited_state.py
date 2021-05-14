from abc import ABC

from src.domain.domainmodel.userstatemachine.states.active_state import ActiveState
from src.domain.domainmodel.userstatemachine.states.user_state import UserState
from src.domain.domainmodel.userstatemachine.states.user_status import UserStatus


class InvitedState(UserState, ABC):
    def get_name(self) -> str:
        return UserStatus.Invited.value

    def active(self) -> UserState:
        return ActiveState()
