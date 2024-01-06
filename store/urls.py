# store/urls.py
from django.urls import path
from .views import store_list, store_detail, menu_price

urlpatterns = [
    path('stores/', store_list, name='store_list'),
    path('stores/<int:store_id>/', store_detail, name='store_detail'),
    path('stores/<int:store_id>/<int:menu_id>/', store_detail, name='store_detail'),
    path('stores/<int:store_id>/<int:menu_id>/price/', menu_price, name='menu_price'),
]

