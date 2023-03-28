from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    balance = models.IntegerField()
    major = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    mbti = models.CharField(max_length=4)
    address = models.CharField(max_length=100)
    