# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # myapp/hello/neo/ => Variable Routing
    path('hello/<str:name>/', views.hello, name='hello'),
    # myapp/ping/
    path('ping/', views.ping, name='ping'),
    # myapp/pong/
    path('pong/', views.pong, name='pong'),
    # myapp/lotto_in/
    path('lotto_in/', views.lotto_in, name='lotto_in'),
    # myapp/lotto_out/
    path('lotto_out/', views.lotto_out, name='lotto_out'),
]
