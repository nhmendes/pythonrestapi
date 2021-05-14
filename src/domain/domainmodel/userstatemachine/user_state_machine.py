from src.domain.domainmodel.userstatemachine.states.initial_state import InitialState
from src.domain.domainmodel.userstatemachine.states.user_state import UserState
from src.domain.domainmodel.userstatemachine.user_state_operations import UserStateOperations


class UserStateMachine(UserStateOperations):
    state: UserState = InitialState()

    def invited(self):
        self.state = self.state.invited()

    def active(self):
        self.state = self.state.active()

    def disabled(self):
        self.state = self.state.disabled()

    def deleted(self):
        self.state = self.state.deleted()

    def get_state_name(self) -> str:
        return self.state.get_name()
