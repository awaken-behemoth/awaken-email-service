from django.urls import path

from . import views

urlpatterns = [
    path('root/', views.index, name='index'),
]