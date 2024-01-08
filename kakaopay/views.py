from django.shortcuts import render, redirect
import requests
import json
from django.template import loader
from django.http import HttpResponse, JsonResponse

def kakaoPay(request):
    return render(request, 'kakaopay.html')
def kakaoPayLogic(request):
    _admin_key = 'e7d2a224f2204042b041e7d646a8e640'
    _url = f'https://kapi.kakao.com/v1/payment/ready'
    _headers = {
        'Authorization': f'KakaoAK {_admin_key}',
    }
    _data = {
        'cid': 'TC0ONETIME',
        'partner_order_id':'partner_order_id',
        'partner_user_id':'partner_user_id',
        'item_name':'비타민 과일 박스 세트',
        'quantity':'1',
        'total_amount':'3000',
        'vat_amount':'0',
        'tax_free_amount':'0',
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
    _admin_key = 'e7d2a224f2204042b041e7d646a8e640'
    _headers = {
        'Authorization': f'KakaoAK {_admin_key}'
    }
    _data = {
        'cid':'TC0ONETIME',
        'tid': request.session['tid'],
        'partner_order_id':'partner_order_id',
        'partner_user_id':'partner_user_id',
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
        return render(request, 'paySuccess.html')
        print(_result)