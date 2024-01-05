# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, logout
from .models import User
from django.http import JsonResponse

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        password = request.POST['password']

        # 이메일이 이미 존재하는지 확인
        if User.objects.filter(email=email).exists():
            return JsonResponse({'message': '이미 가입된 이메일입니다.'})

        # 이메일이 존재하지 않으면 새로운 사용자 생성
        hashed_password = make_password(password)
        user = User(email=email, name=name, phone_number=phone_number, password=hashed_password)
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
