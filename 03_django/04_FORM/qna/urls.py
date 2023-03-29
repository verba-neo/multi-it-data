# qna/urls.py

from django.urls import path
from . import views

app_name = 'qna'

urlpatterns = [
    # No pk(var routing) required
    # qna:create
    path('create/', views.create, name='create'),
    # qna:index``
    path('', views.index, name='index'),

    # var routing => modelname_pk
    # qna:detail
    path('<int:question_pk>/', views.detail, name='detail'),
    # qna:update
    path('<int:question_pk>/update/', views.update, name='update'),
    # qna:delete
    path('<int:question_pk>/delete/', views.delete, name='delete'),
]
