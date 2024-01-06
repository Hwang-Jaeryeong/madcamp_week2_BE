# accounts/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),

    path('kakao/login/', kakao_login, name='kakao_login'),
    path('kakao/login/callback/', kakao_callback, name="kakao_callback"),
]
