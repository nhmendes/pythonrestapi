from src.domain.domainmodel.userstatemachine.states.deleted_state import DeletedState
from src.domain.domainmodel.userstatemachine.states.disabled_state import DisabledState
from src.domain.domainmodel.userstatemachine.states.user_state import UserState
from src.domain.domainmodel.userstatemachine.states.user_status import UserStatus


class ActiveState(UserState):
    def get_name(self) -> str:
        return UserStatus.Active.value

    def disabled(self) -> UserState:
        return DisabledState()

    def deleted(self) -> UserState:
        return DeletedState()
