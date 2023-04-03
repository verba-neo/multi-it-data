from django.db import models


class Posting(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    

class Reply(models.Model):
    content = models.CharField(max_length=200)
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)