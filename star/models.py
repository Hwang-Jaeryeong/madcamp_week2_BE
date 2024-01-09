# star/models.py
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

class Store(models.Model):
    name = models.CharField(max_length=255)

class Star(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)  # 수정
    rating = models.IntegerField()
