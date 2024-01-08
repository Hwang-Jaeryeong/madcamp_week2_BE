from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'kakao'),
    path('kakaoPay/', views.kakaoPay),
    path('kakaoPayLogic/', views.kakaoPayLogic),
    path('paySuccess/', views.paySuccess),
    path('payFail/', views.payFail),
    path('payCancel/', views.payCancel),
    path('methodsCheck/<int:id>', views.methodsCheck),
]