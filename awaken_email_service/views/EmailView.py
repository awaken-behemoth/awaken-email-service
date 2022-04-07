

import json
from django.views import View
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse


class EmailView(View):
    def post(self, request: HttpRequest):

        data = json.loads(request.body)

        recipient_list = data["recipient_list"]
        origin_email = data["origin_email"]
        message = data["message"]
        subject = data["subject"]

        send_mail(subject, message,
                  origin_email, recipient_list)


        return HttpResponse('result')
