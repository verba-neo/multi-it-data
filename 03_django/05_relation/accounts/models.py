# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

from blog.models import Posting


class User(AbstractUser):
    mbti = models.CharField(max_length=4)  # => 컬럼추가 == default 세팅 필요
    like_postings = models.ManyToManyField(Posting, related_name='like_users')  # 테이블 추가


'''
# u1사용자가 좋아한 모든 posting
u1.like_postings.all()

# p1게시글에 좋아한 모든 user
p1.like_users.all()
'''