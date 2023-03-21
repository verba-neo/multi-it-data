# hair/views.py
from django.shortcuts import render
from django.http import HttpResponse


def nice(request):
    # render의 첫번째 인자 => request 고정
    # 두번째 인자 => 템플릿 이름 'str'
    return render(request, 'nice.html')



