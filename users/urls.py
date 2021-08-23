from django.urls import path
from .views import *

urlpatterns = [
    path('', profiles, name='profiles'),
    path('profile/<str:pk>/', user_profile, name='user-profile'),
]