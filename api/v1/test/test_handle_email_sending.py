

import json
import pytest
from flask import Flask
from v1 import get_api_version_1


def test_request_example(client):

    data = json.dumps({
        "template": "password_reset",
        "lang": "password_reset",
        "authority": "no-reply",
        "recipients": ["komlankodoh@gmail.com"]
    })

    response = client.post("/", data=data,
                           content_type="application/json")

    assert response.status_code == 200


def test_should_fail_is_recipients_is_not_provided(client):

    data = json.dumps({
        "template": "good",
        "subject": "I am doing just fine",
        "sending_authority": "no-reply"
    })

    response = client.post("/", data=data,
                           content_type="application/json")

    assert response.status_code == 400
