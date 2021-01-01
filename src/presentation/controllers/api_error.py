""" ApiError """

from dataclasses import dataclass


class ApiError(Exception):
    """ Represents an ApiError to return to the client app """

    def __init__(self, message, status_code, payload=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """ Converts the ApiError to a dictionary format """
        api_error = dict(self.payload or ())
        api_error['message'] = self.message
        return api_error
