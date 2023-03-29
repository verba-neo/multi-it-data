# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),    
    path('', views.index, name='index'),
    path('<int:student_pk>/', views.detail, name='detail'),
    path('<int:student_pk>/update/', views.update, name='update'),
    path('<int:student_pk>/delete/', views.delete, name='delete'),

]
