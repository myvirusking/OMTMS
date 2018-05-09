from django.urls import path
from .views import *

app_name="user"

urlpatterns = [
    path('login/',LoginUser,name='login'),
    path('dashboard/',Dashboard),
    path('logout/',LogoutUser,name='logout'),
    path('registration/',Registration,name='registration'),
    path('movies/',Moveplace,name='movies'),
    path('movies/<int:pk>/<slug:place>/',Moviename,name='movieplace'),
    path('movies/<int:pk>/<slug:place>/<str:moviename>/<slug:language>/',Movieticket,name='movieticket'),
    
]