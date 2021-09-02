from django.urls import path
from .views import *

urlpatterns = [
    path('', get_routes),
    path('projects/', get_projects),
    path('projects/<str:pk>/', get_project),
]