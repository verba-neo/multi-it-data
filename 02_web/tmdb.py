# tmdb
# the movie database

import requests

API_KEY = '05ba6a67212000b04b26783d4cb71e96'

URL = 'https://api.themoviedb.org/3/movie/popular?'
URL += f'api_key={API_KEY}&language=ko-kr'

print(URL)

res = requests.get(URL).json()

popular_movies = res['results']
# 평점순으로 정렬하기
# 성인영화만 필터하기
# 2023년 영화만 필터하기
