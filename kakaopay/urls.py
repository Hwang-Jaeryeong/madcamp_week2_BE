from django.urls import path
from . import views

urlpatterns = [
    path('kakaoPay/', views.kakaoPay),
    path('kakaoPayLogic/', views.kakaoPayLogic),
    path('paySuccess/', views.paySuccess),
    path('payFail/', views.payFail),
    path('payCancel/', views.payCancel),
    # GET | POST - Methods / Params | QueryString
    path('methodsCheck/<int:id>', views.methodsCheck),
]