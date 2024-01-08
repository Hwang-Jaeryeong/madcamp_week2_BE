# store/urls.py
from django.urls import path
from .views import store_list, store_detail, menu_price, rate_store, get_average_rating, menu_list

urlpatterns = [
    path('stores/', store_list, name='store_list'),
    path('stores/<int:store_id>/', store_detail, name='store_detail'),
    path('stores/<int:store_id>/price/<int:menu_id>/', menu_price, name='menu_price'),
    path('star/<int:store_id>/', rate_store, name='rate_store'),
    path('star/<int:store_id>/', get_average_rating, name='get_average_rating'),
    path('menu/', menu_list, name='menu_list'),
]

