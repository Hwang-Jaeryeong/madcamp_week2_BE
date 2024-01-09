# serializers.py
from rest_framework import serializers
from .models import Store, Product, CartItem

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'latitude', 'longitude']

class ProductSerializer(serializers.ModelSerializer):
    store = StoreSerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'store', 'store_name', 'price']

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'store_name', 'quantity', 'price']
