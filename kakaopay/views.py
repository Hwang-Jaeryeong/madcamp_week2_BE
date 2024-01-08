from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
import json
from django.template import loader

def index(request):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
    return render(request, 'index.html', _context)


def kakaoPay(request):
    return render(request, 'kakaopay.html')
def kakaoPayLogic(request):
    _admin_key = 'e7d2a224f2204042b041e7d646a8e640'
    _url = f'https://kapi.kakao.com/v1/payment/ready'
    _headers = {
        'Authorization': f'KakaoAK {_admin_key}',
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    _data = {
        'cid': 'TC0ONETIME',
        'partner_order_id':'1001',
        'partner_user_id':'jryeong67',
        'item_name':'비타민 과일 박스 세트',
        'quantity':'1',
        'total_amount':'3000',
        'tax_free_amount':'0',
        'approval_url':'http://ec2-3-34-151-36.ap-northeast-2.compute.amazonaws.com/paySuccess',
        'fail_url':'http://ec2-3-34-151-36.ap-northeast-2.compute.amazonaws.com/payFail',
        'cancel_url':'http://ec2-3-34-151-36.ap-northeast-2.compute.amazonaws.com/payCancel'
    }
    _res = requests.post(_url, headers=_headers, data=_data)
    _result = _res.json()
    print(_result)
    if 'tid' in _result:
        request.session['tid'] = _result['tid']

    if 'next_redirect_pc_url' in _result:
        return redirect(_result['next_redirect_pc_url'])
    else:
        # Handle the case when the key is not present
        # You can redirect to an error page, display an error message, or take appropriate action
        return HttpResponse("Error: 'next_redirect_pc_url' not found in the result dictionary.")

def paySuccess(request):
    _url = 'https://kapi.kakao.com/v1/payment/approve'
    _admin_key = 'e7d2a224f2204042b041e7d646a8e640'
    _headers = {
        'Authorization': f'KakaoAK {_admin_key}'
    }
    _data = {
        'cid':'TC0ONETIME',
        'tid': request.session['tid'],
        'partner_order_id':'1001',
        'partner_user_id':'jryeong67',
        'pg_token': request.GET['pg_token']
    }
    _res = requests.post(_url, data=_data, headers=_headers)
    _result = _res.json()
    if _result.get('msg'):
        return redirect('/payFail')
    else:
        return render(request, 'paySuccess.html')
        print(_result)


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