


import os
from django.http import HttpResponse
from django.conf import settings

class AuthMiddleware(object):
    def __init__(self, get_response):
        """
        One-time configuration and initialisaton.
        """
        self.get_response = get_response

    def __call__(self, request):
                
        request_auth_token = request.META.get('HTTP_AUTHORIZATION').split(" ")[1];
        
        if (request_auth_token == settings.AWAKEN_EMAIL_SERVICE_AUTHORIZATION_TOKEN):
            response = self.get_response(request)
            return response;
         
        return HttpResponse(status=401,content="unauthorized request")

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Called just before Django calls the view.
        """
        return None

    def process_exception(self, request, exception):
        """
        Called when a view raises an exception.
        """
        return None

    def process_template_response(self, request, response):
        """
        Called just after the view has finished executing.
        """
        return response
