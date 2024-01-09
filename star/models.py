# star/models.py
from django.db import models

class StoreRating(models.Model):
    store_name = models.CharField(max_length=255)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.store_name}: {self.rating}점"