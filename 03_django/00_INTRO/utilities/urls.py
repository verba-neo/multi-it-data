from django.urls import path
from . import views


urlpatterns = [
    # utitlities/get_lotto/
    path('get_lotto/', views.get_lotto),
    # utitlities/this_week/
    path('this_week/', views.this_week),
    # utitlities/check_lotto/
    path('check_lotto/', views.check_lotto),
]
