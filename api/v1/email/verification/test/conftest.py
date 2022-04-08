

import pytest
from flask import Flask

from utils import load_env
from ..blueprint import blueprint

@pytest.fixture()
def app():
    
    app = Flask(__name__)

    # default api endpoint
    app.register_blueprint(blueprint, url_prefix="/")

    # other setup can go here
    with app.app_context():
        load_env()

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()