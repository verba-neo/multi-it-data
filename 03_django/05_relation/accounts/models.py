# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

from blog.models import Posting


class User(AbstractUser):
    # mbti = models.CharField(max_length=4)  # => 컬럼추가 == default 세팅 필요
    like_postings = models.ManyToManyField(Posting, related_name='like_users')  # 테이블 추가
    
    # M:N 에서 'self' 참조일 경우에는 양방향 레코드 기록(symmetrical)이 기본값이다. 
    # symmetrical=False를 줘야 1방향 팔로우 가능
    stars = models.ManyToManyField('self', symmetrical=False, related_name='fans')
    # followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')


'''
# u1사용자가 좋아한 모든 posting
u1.like_postings.all()

# p1게시글에 좋아한 모든 user
p1.like_users.all()
'''