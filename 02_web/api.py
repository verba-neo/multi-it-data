# api.py
import requests

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1058'
res = requests.get(url).json()
print(res)

