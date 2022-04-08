
import os
from flask import Flask
from dotenv import load_dotenv
from utils import load_env;

from v1 import get_api_version_1;


app = Flask(__name__)

# default api endpoint
app.register_blueprint(get_api_version_1("api_default_version"), url_prefix="/api")

app.register_blueprint(get_api_version_1("api_version_1"), url_prefix= "/api/v1")


with app.app_context():
    load_env()

