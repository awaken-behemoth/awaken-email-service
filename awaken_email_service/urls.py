
from django.contrib import admin
from django.urls import include, path

from awaken_email_service.views.EmailView import EmailView

urlpatterns = [
    path("api/email" , EmailView.as_view()),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls'))
]
