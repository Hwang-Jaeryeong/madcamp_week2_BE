# urls.py
from django.urls import path
from .views import view_cart, add_to_cart, remove_from_cart

urlpatterns = [
    path('get_cart/', view_cart, name='view_cart'),
    path('add/', add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_item_order>/', remove_from_cart, name='remove_from_cart'),
]
