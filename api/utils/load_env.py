


import os
from flask import current_app
from dotenv import load_dotenv

load_dotenv()


def load_env():
    
    current_app.config["EMAIL_PORT"] = os.environ["EMAIL_PORT"]
    current_app.config["EMAIL_HOST"] = os.environ["EMAIL_HOST"];
    current_app.config["EMAIL_HOST_USER"] = os.environ["EMAIL_HOST_USER"]
    current_app.config["EMAIL_HOST_PASSWORD"] = os.environ["EMAIL_HOST_PASSWORD"]
    current_app.config["AWAKEN_EMAIL_SERVICE_AUTHORIZATION_TOKEN"] = os.environ["AWAKEN_EMAIL_SERVICE_AUTHORIZATION_TOKEN"]