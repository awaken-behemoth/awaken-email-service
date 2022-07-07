
from flask import Flask
from utils import load_env
from flask import current_app
from v1 import get_api_version_1


app = Flask(__name__)

# default api endpoint
app.register_blueprint(
    get_api_version_1("api_default_version"),
    url_prefix="/api")

app.register_blueprint(
    get_api_version_1("api_version_1"),
    url_prefix="/api/v1")


@app.route("/")
def greeting():
    """_summary_

    Returns:
        _type_: _description_
    """
    return "I am glad to have you here"


with app.app_context():
    load_env()


if __name__ == '__main__':
    PORT: int = current_app.config["PORT"]
    app.run(port=PORT, debug=True, host='0.0.0.0')
