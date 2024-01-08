# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    current_location = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        # 비밀번호를 해시화하여 저장
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)