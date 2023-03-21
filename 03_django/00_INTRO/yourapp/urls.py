from django.urls import path
from . import views

urlpatterns = [
    # yourapp/index/
    path('index/', views.index),
]