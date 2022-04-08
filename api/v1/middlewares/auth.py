
from flask import Blueprint, Flask, current_app, request

from v1.errors import Unauthorized


def assert_authorization_header_is_valid(authorization_header: str):
    if authorization_header is None:
        raise Unauthorized("Not authorization header present in request header")
    
    split_authorization_header = authorization_header.split(' ')
    
    if len(split_authorization_header) != 2 :
        raise Unauthorized("Misformed header token.")
    
    [token_type, token] = split_authorization_header;

    if token_type != "Bearer" :
        raise Unauthorized("Misformed header token. Expected Bearer token")

    if token != current_app.config["AWAKEN_EMAIL_SERVICE_AUTHORIZATION_TOKEN"]:
        raise Unauthorized("Invalid token")
    
    print("all the thest passed and he is authorized")
    return


def add_auth_middlename(app: Blueprint):
    """ Adds authentication to request. Verify is the request is allowed by checking if
        the bearer token is the same;
    """
    
    # registration of authentication middle ware on app instance
    @app.before_request
    def before_request():

        authorization_header = request.headers.get('Authorization')

        assert_authorization_header_is_valid(authorization_header)
