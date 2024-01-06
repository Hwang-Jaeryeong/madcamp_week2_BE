# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, logout
from django.http import JsonResponse
import urllib.parse  # urllib.parse를 import 추가
from .models import User

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        latitude = request.POST.get('latitude')  # 새로 추가한 필드
        longitude = request.POST.get('longitude')  # 새로 추가한 필드

        # 이메일이 이미 존재하는지 확인
        if User.objects.filter(email=email).exists():
            return JsonResponse({'message': 'This email is already signed up.'})

        # 이메일이 존재하지 않으면 새로운 사용자 생성
        hashed_password = make_password(password)
        user = User(email=email, name=name, phone_number=phone_number, password=hashed_password,
                    latitude=latitude, longitude=longitude)  # 위치 정보 추가
        user.save()

        return JsonResponse({'message': 'Success Signup!'})

    return render(request, 'signup.html')


from django.shortcuts import render
from django.http import JsonResponse

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                return JsonResponse({'message': 'Success Login!'})
            else:
                return JsonResponse({'message': 'Fail Login'})
        except User.DoesNotExist:
            return JsonResponse({'message': 'Failed'})

    return render(request, 'signin.html')

def signout(request):
    logout(request)
    return JsonResponse({'message': 'Success Logout!'})


# code 요청
def kakao_login(request):
    app_rest_api_key = "aff295bb2c86c694086dd2c6139affc3"  # 문자열을 따옴표로 감싸야 합니다.
    redirect_uri = "http://127.0.0.1:8000/accounts/kakao/login/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
    )

def kakao_callback(request):
    params = urllib.parse.urlencode(request.GET)
    return redirect(f'http://127.0.0.1:8000/accounts/kakao/login/callback?{params}')