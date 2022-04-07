

from flask import Blueprint, request, jsonify
from flask_expects_json import expects_json


def get_api_version_1(name):
    
    api = Blueprint(name, name)

    email_sending_schema = {
        "type": "object",
        "properties": {
            "template": {type: "string"},
            "subject": {"type": "string"},
            "sending_authority": {"type": "string"},
            "recipients": {"type": "array", "minItems": 1},
        },
        "required": ["template", "subject", "sending_authority", "recipients"]
    }

    @api.post("/")
    @expects_json(email_sending_schema)
    def handle_email_sending():

        email_details = request.json

        print(email_details)

        return email_details
    
    return api;
