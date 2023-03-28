from django.db import models


MBTI_CHOICES = [
    # 저장값, 보이는값
    ('ENTP', 'ENTP'),
    ('ESFJ', 'ESFJ'),
    ('ISTJ', 'ISTJ'),
    ('INFP', 'INFP'),
]

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    balance = models.IntegerField()
    major = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    mbti = models.CharField(max_length=4, choices=MBTI_CHOICES)
    address = models.CharField(max_length=100)
    
