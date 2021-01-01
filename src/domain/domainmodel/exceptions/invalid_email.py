class InvalidEmail(Exception):
    """Exception raised for invalid email formats.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Invalid email format"):
        self.message = message
        super().__init__(self.message)
