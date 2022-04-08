

from v1 import email_service
from flask import Blueprint, request
from v1.email_service import send_email
from flask_expects_json import expects_json



def get_api_version_1(name):
    api = Blueprint(name, name)

    email_sending_schema = {
        "type": "object",
        "properties": {
            "lang": {"type": "string"},
            "template": {"type": "string"},
            "authority": {"type": "string"},
            "recipients": {"type": "array", "minItems": 1},
        },
        "required": ["template", "lang", "authority", "recipients"]
    }

    @api.post("/")
    @expects_json(email_sending_schema)
    def handle_email_sending():

        email_details = request.json

        email = email_service.Email( email_details["template"], email_details["lang"])
        
        recipients = email_details["recipients"];
        authority = email_details["authority"];
        
        email_service.send_email(recipients, email, authority);
        
        return "";

    return api
