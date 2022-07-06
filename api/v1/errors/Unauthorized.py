
from .CustomError import CustomError


class Unauthorized(CustomError):
    code = 401
    status = "UNAUTHORIZED"
    description = "You do not have permission to access this ressource"

    def __init__(self, description):
        self.description = description
