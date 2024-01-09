# store/urls.py
from django.urls import path
from .views import store_list, store_detail, add_store_menu, rate_store, get_average_rating, menu_list

urlpatterns = [
    path('stores/', store_list, name='store_list'),
    path('stores/<int:store_id>/', store_detail, name='store_detail'),
    path('star/<int:store_id>/', rate_store, name='rate_store'),
    path('star/<int:store_id>/', get_average_rating, name='get_average_rating'),
    path('menu/', menu_list, name='menu_list'),
    path('add_store_menu/', add_store_menu, name='add_store_menu'),
]

