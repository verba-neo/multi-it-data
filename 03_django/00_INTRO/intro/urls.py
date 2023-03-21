# Master URLs (intro/urls.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # 접두사가, 'myapp/'이면, myapp/urls.py로 던질래
    path('myapp/', include('myapp.urls')),
    # 접두사가 'hair/'면, hair/urls.py 로 던질래
    path('hair/', include('hair.urls')),
    path('yourapp/', include('yourapp.urls')),
    path('utilities/', include('utilities.urls')),
]

