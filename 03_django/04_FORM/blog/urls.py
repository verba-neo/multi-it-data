# blog/urls.py

from django.urls import path
from . import views

# 'app_name:name'

app_name = 'blog'

urlpatterns = [
    # blog:create
    path('create/', views.create, name='create'),    
    # blog:index
    path('', views.index, name='index'),
    # blog:detail
    path('<int:student_pk>/', views.detail, name='detail'),
    # blog:update
    path('<int:student_pk>/update/', views.update, name='update'),
    # blog:delete
    path('<int:student_pk>/delete/', views.delete, name='delete'),

]
