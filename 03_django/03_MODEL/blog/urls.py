# blog/urls.py

from django.urls import path
from . import views


urlpatterns = [
    # Create
    # blog/new/
    path('new/', views.new, name='new'),
    # blog/create/ [사용자 입력 데이터]
    path('create/', views.create, name='create'),

    # Read
    # blog/
    path('', views.index, name='index'),
    # blog/1/
    path('<int:x>/', views.detail, name='detail'),


    # Update
    # blog/1/edit/
    path('<int:x>/edit/', views.edit, name='edit'),
    # blog/1/update/
    path('<int:x>/update/', views.update, name='update'),

    # Delete
    # blog/1/delete/
    path('<int:x>/delete/', views.delete, name='delete'),
]
