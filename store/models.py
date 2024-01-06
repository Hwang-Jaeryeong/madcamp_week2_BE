# store/models.py
from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Menu(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    remaining_quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=255)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    remaining_quantity = models.IntegerField()
    detail_name1 = models.CharField(max_length=255, null=True, blank=True)
    detail_gram1 = models.CharField(max_length=255, null=True, blank=True)
    detail_name2 = models.CharField(max_length=255, null=True, blank=True)
    detail_gram2 = models.CharField(max_length=255, null=True, blank=True)
    detail_name3 = models.CharField(max_length=255, null=True, blank=True)
    detail_gram3 = models.CharField(max_length=255, null=True, blank=True)

    def as_dict(self):
        return {
            "name": self.name,
            "remaining_quantity": self.remaining_quantity,
            "details": {
                "detail_name1": self.detail_name1,
                "detail_gram1": self.detail_gram1,
                "detail_name2": self.detail_name2,
                "detail_gram2": self.detail_gram2,
                "detail_name3": self.detail_name3,
                "detail_gram3": self.detail_gram3,
            }
        }

class Price(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.menu.name} - {self.price}"

class Price(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.menu.name} - {self.price}"
