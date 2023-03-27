from django.urls import path
from . import views

urlpatterns = [
    # Create
    # /board/new/
    path('new/', views.new, name='new'),
    # /board/create/
    path('create/', views.create, name='create'),

    # Read
    # /board/
    path('', views.index, name='index'),
    # /board/1/
    path('<int:notice_pk>/', views.detail, name='detail'),

    # Update
    # /board/1/edit/
    path('<int:notice_pk>/edit/', views.edit, name='edit'),
    # /board/1/update/
    path('<int:notice_pk>/update/', views.update, name='update'),
         
    # Delete
    # /board/1/delete/
    path('<int:notice_pk>/delete/', views.delete, name='delete'),
]
