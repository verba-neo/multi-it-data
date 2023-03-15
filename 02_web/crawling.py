# crawling.py
# pip install requests
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup


def get_real_lotto():
    url = 'https://search.naver.com/search.naver?&query=%EB%A1%9C%EB%98%90'
    # 요청은 클라이언트 프로그램을 통해 URL로 보낸다
    res = requests.get(url)
    data = BeautifulSoup(res.text, 'html.parser')
    real_numbers = []

    for tag in data.select('.ball'):
        real_numbers.append(tag.text)

    real_numbers = list(map(int, real_numbers))
    bonus_number = real_numbers.pop()
    return real_numbers, bonus_number

    # list(map(lambda tag: int(tag.text), data.select('.ball')))
    # return {'real_numbers': real_numbers, 'bonus_number': bonus_number}
