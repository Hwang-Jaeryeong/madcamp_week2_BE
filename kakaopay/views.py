from django.shortcuts import render, redirect
import requests
import json
from django.template import loader
from django.http import HttpResponse, JsonResponse


def index(request):
    _context = {'check': False}
    if request.session.get('access_token'):
        _context['check'] = True
    return render(request, 'index.html', _context)


def kakaoPay(request):
    return render(request, 'kakaopay.html')


def kakaoPayLogic(request):
    _admin_key = 'e7d2a224f2204042b041e7d646a8e640'  # 입력필요
    _url = f'https://kapi.kakao.com/v1/payment/ready'
    _headers = {
        'Authorization': f'KakaoAK {_admin_key}',
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    _data = {
        'cid': 'TC0ONETIME',
        'partner_order_id': '1001',
        'partner_user_id': 'jryeong67',
        'item_name': '비타민 과일 박스 세트',
        'quantity': '1',
        'total_amount': '3000',
        'tax_free_amount': '0',
        # 내 애플리케이션 -> 앱설정 / 플랫폼 - WEB 사이트 도메인에 등록된 정보만 가능합니다
        # * 등록 : http://IP:8000
        'approval_url':'http://ec2-3-34-151-36.ap-northeast-2.compute.amazonaws.com/paySuccess',
        'fail_url':'http://ec2-3-34-151-36.ap-northeast-2.compute.amazonaws.com/payFail',
        'cancel_url':'http://ec2-3-34-151-36.ap-northeast-2.compute.amazonaws.com/payCancel'
    }
    _res = requests.post(_url, data=_data, headers=_headers)
    _result = _res.json()
    request.session['tid'] = _result['tid']
    return redirect(_result['next_redirect_pc_url'])


def paySuccess(request):
    _url = 'https://kapi.kakao.com/v1/payment/approve'
    _admin_key = 'e7d2a224f2204042b041e7d646a8e640'  # 입력필요
    _headers = {
        'Authorization': f'KakaoAK {_admin_key}'
    }
    _data = {
        'cid': 'TC0ONETIME',
        'tid': request.session['tid'],
        'partner_order_id': 'partner_order_id',
        'partner_user_id': 'partner_user_id',
        'pg_token': request.GET['pg_token']
    }
    _res = requests.post(_url, data=_data, headers=_headers)
    _result = _res.json()
    if _result.get('msg'):
        return redirect('/payFail')
    else:
        # * 사용하는 프레임워크별 코드를 수정하여 배포하는 방법도 있지만
        #   Req Header를 통해 분기하는 것을 추천
        # - Django 등 적용 시
        print(_result)
        return render(request, 'paySuccess.html')

        # - React 적용 시
        # return redirect('http://localhost:3000')

def payFail(request):
    return render(request, 'payFail.html')


def payCancel(request):
    return render(request, 'payCancel.html')


def methodsCheck(request, id):
    if (request.method == 'GET'):
        print(f"GET QS : {request.GET.get('data', '')}")
        print(f"GET Dynamic Path : {id}")

    # PostMan으로 Localhost 테스트를 위해 CSRF 해제
    # project/settings.py 파일에서
    # MIDDLEWARE -> 'django.middleware.csrf.CsrfViewMiddleware' 주석 처리
    elif (request.method == 'POST'):
        print(f"POST QS : {request.GET.get('data', '')}")
        print(f"POST Dynamic Path : {id}")
        return HttpResponse("POST Request.", content_type="text/plain")
    return render(request, 'methodGet.html')