from django.db import models


# Table
class Notice(models.Model):
    # Column
    title = models.CharField(max_length=200)
    content = models.TextField()
    rank = models.IntegerField()
