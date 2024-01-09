# cart/models.py
# models.py
from django.conf import settings
from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

class Product(models.Model):
    name = models.CharField(max_length=255)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255)

class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255)
    price = models.IntegerField()



