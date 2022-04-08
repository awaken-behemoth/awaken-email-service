
import pytest
from flask import Flask
from v1 import middlewares, errors

TEST_TOKEN = "some_random_supper_long_suit_of_string"


@pytest.fixture()
def test_client():
    app = Flask(__name__)

    app.config["AWAKEN_EMAIL_SERVICE_AUTHORIZATION_TOKEN"] = TEST_TOKEN

    middlewares.auth.add_auth_middlename(app)
    errors.register_custom_errors_handlers(app)

    @app.post("/")
    def dummy_handler():
        return ""

    return app.test_client()


def test_should_return_unauthorized_when_token_is_not_provided(test_client):
    response = test_client.post("/")

    print(response)
    assert response.status_code == 401


def test_should_return_unauthorized_when_using_wrong_authorization_specification(test_client):
    response = test_client.post(
        "/", headers={"Authorization": "Basic email_password"})

    assert response.status_code == 401

def test_should_return_401_if_the_token_if_misformated(test_client):
    response = response = test_client.post(
        "/", headers={"Authorization": "Bearer misformed token containing spaces"})

    assert response.status_code == 401

def test_should_return_ok_when_using_corrent_token(test_client):
    response = test_client.post(
        "/", headers={"Authorization": "Bearer "+  TEST_TOKEN})
    
    assert response.status_code == 200
