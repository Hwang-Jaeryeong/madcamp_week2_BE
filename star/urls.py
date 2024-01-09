# star/urls.py

from django.urls import path
from .views import post_star, get_average_rating

urlpatterns = [
    path('star/', post_star, name='post_star'),
    path('average_rating/', get_average_rating, name='get_average_rating'),
]
