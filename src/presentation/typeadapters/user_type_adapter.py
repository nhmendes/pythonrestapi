from src.domain.domainmodel.user import User as DomainUser
from src.domain.domainmodel.email import Email
from src.presentation.models.user import User


class UserTypeAdapter:
    def to_domain(self) -> DomainUser:
        """ Converts from UpdateUserRequest to the domain User datatype """
        return DomainUser(
            user_id=self.user_id,
            username=self.username,
            name=self.name,
            email=Email(self.email))

    def from_domain(self, domain_user: DomainUser):
        print(domain_user)
        return User(
            user_id=domain_user.user_id,
            username=domain_user.username,
            name=domain_user.name,
            email=domain_user.email)
