from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return {
        "dict": "that is the thing",
        "learn" : "that is another thing"
    }