from src.domain.domainmodel.userstatemachine.states.active_state import ActiveState
from src.domain.domainmodel.userstatemachine.states.deleted_state import DeletedState
from src.domain.domainmodel.userstatemachine.states.user_state import UserState
from src.domain.domainmodel.userstatemachine.states.user_status import UserStatus


class DisabledState(UserState):
    def get_name(self) -> str:
        return UserStatus.Disabled.value

    def active(self) -> UserState:
        return ActiveState()

    def deleted(self) -> UserState:
        return DeletedState()
