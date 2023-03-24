# blog/urls.py

from django.urls import path
from . import views


urlpatterns = [
    # Create
    # blog/new/
    path('new/', views.new, name='new'),
    # blog/create/
    path('create/', views.create, name='create'),

    # Read
    # blog/
    path('', views.index, name='index'),
    # blog/1/
    path('<int:article_pk>/', views.detail, name='detail'),

]
