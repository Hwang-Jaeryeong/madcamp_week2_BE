# accounts/urls.py
from django.urls import path
from .views import NaverLoginView

urlpatterns = [
    path('accounts/naver/login/', NaverLoginView.as_view(), name='naver_login'),

]
