# hair/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # hair/nice/ => views.py의 nice 함수를 실행해라.
    path('nice/', views.nice)
]