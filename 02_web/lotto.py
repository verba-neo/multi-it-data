import crawling  # ./crawling.py 를 가져온다.
import random

real_numbers, bonus_number = crawling.get_real_lotto()

cnt = {
    'all': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
}

while 1:
    cnt['all'] += 1
    lucky_numbers = random.sample(range(1, 46), 6)
    match_count = len(set(lucky_numbers) & set(real_numbers))

    if match_count == 6:
        print('1등!', cnt)
        break
    elif match_count == 5 and bonus_number in lucky_numbers:
        cnt['2'] += 1
        # print('2등')
    elif match_count == 5:
        cnt['3'] += 1
    elif match_count == 4:
        cnt['4'] += 1
        # print('4등')
    elif match_count == 3:
        cnt['5'] += 1
        # print('5등')


