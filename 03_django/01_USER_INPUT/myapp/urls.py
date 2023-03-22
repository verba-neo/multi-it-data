# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # myapp/ping/
    path('ping/', views.ping),
    # myapp/pong/
    path('pong/', views.pong),
]
