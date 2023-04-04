# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # mbti = models.CharField(max_length=4)
    pass