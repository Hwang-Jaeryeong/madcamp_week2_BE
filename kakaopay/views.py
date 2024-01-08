from django.shortcuts import render, redirect
import requests

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
    if 'tid' in _result:
        request.session['tid'] = _result['tid']
    else:
    # Handle the case when 'tid' key is not present, possibly by providing a default value or raising an appropriate exception.
    # For example:
    # request.session['tid'] = None  # Provide a default value
    # Or raise an exception:
    # raise KeyError("'tid' key not found in _result dictionary")

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