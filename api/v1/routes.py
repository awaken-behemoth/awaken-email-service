

from v1 import email
from flask import Blueprint, request


def get_api_version_1(name):
    api = Blueprint(name, name)

    api.register_blueprint(email.verification.blueprint,
                           url_prefix='/email/email-verification')

    return api
