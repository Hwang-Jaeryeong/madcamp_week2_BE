# cart/serializers.py
from rest_framework import serializers
from .models import CartItem
from store.serializers import StoreSerializer  # Import StoreSerializer

class CartItemSerializer(serializers.ModelSerializer):
    store = StoreSerializer()  # Use StoreSerializer for store field

    class Meta:
        model = CartItem
        fields = ['id', 'product_name', 'price', 'store']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['store_name'] = representation['store']['name']
        return representation
