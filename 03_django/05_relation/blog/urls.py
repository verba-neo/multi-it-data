from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # blog/create/
    path('create/', views.create_posting, name='create_posting'),
    # blog/
    path('', views.posting_index, name='posting_index'),
    # blog/1/
    path('<int:posting_pk>/', views.posting_detail, name='posting_detail'),
    # blog/1/update/
    path('<int:posting_pk>/update/', views.update_posting, name='update_posting'),
    # blog/1/delete/
    path('<int:posting_pk>/delete/', views.delete_posting, name='delete_posting'),

    # blog/1/replies/create/
    path('<int:posting_pk>/replies/create/', views.create_reply, name='create_reply'),
]
