import requests
from django.shortcuts import render


# name => Variable Routing
def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'myapp/hello.html', context)


def ping(request):
    return render(request, 'myapp/ping.html')


def pong(request):
    # POST 방식
    # 1. <form method="POST">
    # 2. <form> > {% csrf_token %}
    # 3. view => request.POST
    context = {
        'name': request.POST['myname'],
        'age': request.POST['age'],
        'mbti': request.POST['mbti'],
    }
    return render(request, 'myapp/pong.html', context)


def lotto_in(request):
    return render(request, 'myapp/lotto_in.html')


def lotto_out(request):
    draw_no = request.GET['draw_no']
    URL = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={draw_no}'
    res = requests.get(URL).json()

    numbers = [value for key, value in res.items() if 'drwtNo' in key]
    numbers.sort()
    bonus_no = res['bnusNo']

    context = {
        'draw_no': draw_no,
        'numbers': numbers,
        'bonus_no': bonus_no,
    }

    return render(request, 'myapp/lotto_out.html', context)

