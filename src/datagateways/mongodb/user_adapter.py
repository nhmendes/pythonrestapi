""" Users adapter """


from domain.domainmodel.user import User


class UserAdapter:
    """ User data type adapter from and to domain """

    @staticmethod
    def to_domain() -> User:
        """ converts a database User data type model to the domain User representation """
        print("adapted from db model to domain")

    @staticmethod
    def to_db_model():
        """ converts a domain User data type model to the database User representation """
        print("adapted from domain to db model")
