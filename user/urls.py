from django.urls import path
from .views import *

app_name="user"

urlpatterns = [
    path('login/',LoginUser,name='login'),
    path('dashboard/',Dashboard),
    path('logout/',LogoutUser,name='logout'),
    path('registration/',Registration,name='registration'),
    path('movietheater/',Movietheater,name='movietheater'),
    path('movietheater/<int:pk>/moviename/',Moviename,name='moviename'),
]
