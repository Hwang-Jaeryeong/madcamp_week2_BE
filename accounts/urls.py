# accounts/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('kakao/login/', kakao_login, name='kakao_login'),
    path('kakao/login/callback/', kakao_callback, name="kakao_callback"),
]