import requests
import random

from django.shortcuts import render

def get_lotto(request):
    lucky_numbers = random.sample(range(1, 46), 6)
    lucky_numbers.sort()
    context = {
        'lucky_numbers': lucky_numbers,
    }

    return render(request, 'utilities/get_lotto.html', context)


def this_week(request):
    URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1059'
    res = requests.get(URL).json()
    print(res)
    return render(request, 'utilities/this_week.html')


def check_lotto(request):

    return render(request, 'utilities/check_lotto.html')