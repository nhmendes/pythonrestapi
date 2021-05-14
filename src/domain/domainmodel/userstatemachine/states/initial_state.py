from abc import ABC

from src.domain.domainmodel.userstatemachine.states.active_state import ActiveState
from src.domain.domainmodel.userstatemachine.states.invited_state import InvitedState
from src.domain.domainmodel.userstatemachine.states.user_state import UserState


class InitialState(UserState, ABC):
    def get_name(self) -> str:
        return ""

    def invited(self) -> UserState:
        return InvitedState()

    def active(self) -> UserState:
        return ActiveState()
