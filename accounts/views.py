# views.py
from django.shortcuts import redirect
import urllib


# code 요청
def kakao_login(request):
    app_rest_api_key = "aff295bb2c86c694086dd2c6139affc3"
    redirect_uri = "http://127.0.0.1:8000/accounts/kakao/login/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
    )


# access token 요청
def kakao_callback(request):
    params = urllib.parse.urlencode(request.GET)
    return redirect(f'http://127.0.0.1:8000/accounts/kakao/login/callback?{params}')