

import datetime
from flask import Blueprint
from .CustomError import CustomError
from .Unauthorized import Unauthorized


def register_custom_errors_handlers(app: Blueprint):
    """Registers all errors handlers derived from the custom error handler class;

    Args:
        app (Blueprint): blueprint or app that can register error handler

    Returns:
        _type_: void
    """
    @app.errorhandler(CustomError)
    def custom_error_handler(error):

        response = {
            "message": error.description,
            "status": error.status,
            "timestamp": datetime.datetime.now()
        }

        return response, error.code
