# cart/serializers.py
from rest_framework import serializers
from .models import CartItem, Order

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product_name', 'price', 'store_name']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'product_name', 'store_name', 'price', 'created_at']