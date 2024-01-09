# star/urls.py
from django.urls import path
from .views import get_store_average_rating, add_store_rating

urlpatterns = [
    path('average_rating/', get_store_average_rating, name='get_store_average_rating'),
    path('add_rating/', add_store_rating, name='add_store_rating'),
]
