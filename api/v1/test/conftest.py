

import pytest
from flask import Flask
from v1 import get_api_version_1

@pytest.fixture()
def app():
    blueprint = get_api_version_1("api_version_1_test")
    app = Flask(__name__)

    # default api endpoint
    app.register_blueprint(blueprint, url_prefix="")

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()