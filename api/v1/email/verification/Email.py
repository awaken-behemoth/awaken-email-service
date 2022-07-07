
from api.v1.email.Email import Email
from email.mime.text import MIMEText

data_schema = {
    "validation-url": {"type": "string"}
}


class Email(Email):
    message: str = ""

    def get_message(self):

        language = self.lang

        validation_url = self.data["validation-url"]

        message = f'Click the link {validation_url} to activate your account; translated in {language}'

        return MIMEText(message)

    def get_subject(self):

        return "Email password reset"

    def get_authority_email(self):

        return "no-reply@gmail.com"
