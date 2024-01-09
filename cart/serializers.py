# cart/serializers.py
from rest_framework import serializers
from .models import CartItem
from store.serializers import StoreSerializer  # StoreSerializer를 import

class CartItemSerializer(serializers.ModelSerializer):
    store = StoreSerializer()  # StoreSerializer를 사용하여 store 필드를 시리얼화

    class Meta:
        model = CartItem
        fields = ['id', 'product_name', 'price', 'store']  # store 필드를 포함

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['store_name'] = representation['store']['name']
        return representation

