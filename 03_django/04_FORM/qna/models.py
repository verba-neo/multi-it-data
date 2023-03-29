from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    reward = models.IntegerField()
    