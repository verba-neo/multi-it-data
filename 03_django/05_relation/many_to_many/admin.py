from django.contrib import admin
from .models import Album, Artist, Song

# Register your models here.
admin.site.register([Album, Artist, Song])

# python manage.py createsuperuser
# 127.0.0.1:8000/admin
# login => 직접 입력
# Artist / Album / Song