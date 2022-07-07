from flask import Blueprint

from v1 import middlewares, errors, email


def get_api_version_1(name):
    api = Blueprint(name, name)

    # middlewares set up
    middlewares.auth.add_auth_middlename(api)

    # custom error handler registration
    errors.register_custom_errors_handlers(api)

    api.register_blueprint(email.verification.blueprint,
                           url_prefix='/email/email-verification')

    return api
