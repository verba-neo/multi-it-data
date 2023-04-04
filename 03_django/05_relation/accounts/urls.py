# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # 회원가입
    path('signup/', views.signup, name='signup'),
    # 로그인
    path('signin/', views.signin, name='signin'),
    # 로그아웃
    path('signout/', views.signout, name='signout'),
]
