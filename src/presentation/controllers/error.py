from dataclasses import dataclass


@dataclass
class Error:
    code: str
    detail: str


class ApiError(Exception):

    def __init__(self, message, status_code, payload=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        api_error = dict(self.payload or ())
        api_error['message'] = self.message
        return api_error
