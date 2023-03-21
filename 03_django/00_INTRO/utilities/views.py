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
    real_numbers = []

    for k, v in res.items():
        if 'drwtNo' in k:
            real_numbers.append(v)

    # for i in range(1, 7):
    #     real_numbers.append(res[f'drwtNo{i}'])

    real_numbers.sort()
    context = {
        'real_numbers': real_numbers,
        'bonus_number': res['bnusNo'],
    }
    return render(request, 'utilities/this_week.html', context)


def check_lotto(request):
    URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1059'
    res = requests.get(URL).json()
    real_numbers = []

    for k, v in res.items():
        if 'drwtNo' in k:
            real_numbers.append(v)
    bonus_number = res['bnusNo']

    lucky_numbers = random.sample(range(1, 46), 6)

    match_count = len(set(lucky_numbers) & set(real_numbers))

    if match_count == 6:
        result = '1등'
    elif match_count == 5 and bonus_number in lucky_numbers:
        result = '2등'
    elif match_count == 5:
        result = '3등'
    elif match_count == 4:
        result = '4등'
    elif match_count == 3:
        result = '5등'
    else:
        result = ':('

    context = {
        'result': result,
        'real_numbers': real_numbers,
        'bonus_number': bonus_number,
        'lucky_numbers': lucky_numbers,
    }    
    
    return render(request, 'utilities/check_lotto.html', context)