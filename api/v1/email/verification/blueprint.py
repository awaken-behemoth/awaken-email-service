

from v1 import email
from .Email import data_schema, Email
from flask import Blueprint, request
from flask_expects_json import expects_json

blueprint = Blueprint("email-verification", "email-verification")

email_sending_schema = {
    "type": "object",
    "properties": {
            "data": data_schema,
            "lang": {"type": "string"},
            "recipient": {"type": "string"},
    },
    "required": ["lang", "data", "recipient"]
}


@blueprint.post("")
@expects_json(email_sending_schema)
def handle_email_confirmation():

    email_details = request.json

    email_to_send = Email(
        email_details["lang"], email_details["data"])

    recipient = email_details["recipient"]

    email.send_email([recipient], email_to_send)

    return ""
