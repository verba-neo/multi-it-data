# myapp/urls.py

from django.urls import path
# 현재 파일 위치와 같은 위치에
# views.py를 import
from . import views

urlpatterns = [
    # myapp/hello/
    path('hello/', views.hello),
    # myapp/bye/
    path('bye/', views.bye),
    # myapp/review/
    path('review/', views.review),
    # myapp/index/
    path('index/', views.index),
]

# /myapp/review/ => review 뷰 함수 실행 => review.html 을 화면에 보여줌
# review.html 에는 오늘 배운 내용을 정리해서 HTML로 작성하세요