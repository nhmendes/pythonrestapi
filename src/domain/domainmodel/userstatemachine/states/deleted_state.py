from src.domain.domainmodel.userstatemachine.states.user_state import UserState
from src.domain.domainmodel.userstatemachine.states.user_status import UserStatus


class DeletedState(UserState):
    def get_name(self) -> str:
        return UserStatus.Deleted.value
