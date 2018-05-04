from django.urls import path
from .views import *

app_name="user"

urlpatterns = [
    path('login/',LoginUser,name='login'),
    path('dashboard/',Dashboard),
    path('logout/',LogoutUser,name='logout'),
    path('registration/',Registration,name='registration'),
    path('movies/',Moveplace,name='movies'),
    path('movies/<slug:place>/',Moviename,name='movieplace'),
    #path('movies/<slug:place>/moviename/',Moviename,name='moviename'),
    
]
