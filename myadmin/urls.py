from django.urls import path
from .views import *

app_name='myadmin'

urlpatterns = [
    path('login/',Myadminlogin,name='login'),
]