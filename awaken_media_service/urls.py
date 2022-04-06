from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('email_services/', include('email_service.urls')),
    path('admin/', admin.site.urls),
]