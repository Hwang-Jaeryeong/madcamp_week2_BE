# store/urls.py
from django.urls import path
from .views import store_list, store_detail, add_store_menu, menu_list

urlpatterns = [
    path('stores/', store_list, name='store_list'),
    path('stores/<int:store_id>/', store_detail, name='store_detail'),
    path('menu/', menu_list, name='menu_list'),
    path('add_store_menu/', add_store_menu, name='add_store_menu'),
]

