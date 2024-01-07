# accounts/models.py

# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    current_location = models.CharField(max_length=255, blank=True)

