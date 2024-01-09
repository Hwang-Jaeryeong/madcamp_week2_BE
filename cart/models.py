# cart/models.py
from django.conf import settings
from django.db import models
from store.models import Store  # Import Store model

class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)


