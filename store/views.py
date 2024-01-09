# store/views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from .models import Store, Menu, Price
from django.shortcuts import render

def store_list(request):
    stores = Store.objects.all()
    store_dict = {store.name: store.id for store in stores}
    return JsonResponse(store_dict)

def menu_price(request, store_id, menu_id):
    try:
        price = Price.objects.get(menu__store_id=store_id, menu_id=menu_id)
    except Price.DoesNotExist:
        return JsonResponse({"error": "가격을 찾을 수 없습니다."}, status=404)

    return JsonResponse({"가격": price.price})

def get_menu_price(menu_id):
    try:
        price = Price.objects.get(menu_id=menu_id)
        return price.price
    except Price.DoesNotExist:
        return None

def menu_list(request):
    menus = Menu.objects.all()
    menu_list = []

    for menu in menus:
        store = get_object_or_404(Store, id=menu.store.id)
        menu_data = {
            "menu_id": menu.id,
            "name": menu.name,
            "store_id": menu.store.id,
            "store_name": store.name,  # Include the store name in the menu data
            "remaining_quantity": menu.remaining_quantity,
            "details": {
                "detail_name1": menu.detail_name1,
                "detail_gram1": menu.detail_gram1,
                "detail_name2": menu.detail_name2,
                "detail_gram2": menu.detail_gram2,
                "detail_name3": menu.detail_name3,
                "detail_gram3": menu.detail_gram3,
            },
            "price": get_menu_price(menu.id)
        }
        menu_list.append(menu_data)

    return JsonResponse(menu_list, safe=False)


def store_detail(request, store_id, menu_id=None):
    store = get_object_or_404(Store, id=store_id)

    if menu_id is not None:
        menu = get_object_or_404(Menu, store_id=store_id, id=menu_id)
        response_data = menu.as_dict(include_menu_id=True)
    else:
        menus = Menu.objects.filter(store_id=store_id)
        store_name = store.name
        latitude = store.latitude
        longitude = store.longitude

        menu_list = [
            {
                "menu_id": menu.id,
                "name": menu.name,
                "remaining_quantity": menu.remaining_quantity,
                "details": {
                    "detail_name1": menu.detail_name1,
                    "detail_gram1": menu.detail_gram1,
                    "detail_name2": menu.detail_name2,
                    "detail_gram2": menu.detail_gram2,
                    "detail_name3": menu.detail_name3,
                    "detail_gram3": menu.detail_gram3,
                }
            }
            for menu in menus
        ]

        response_data = {
            "store_name": store_name,
            "latitude": latitude,
            "longitude": longitude,
            "menus": menu_list
        }

    return JsonResponse(response_data)







@csrf_exempt
def add_store_menu(request):
    if request.method == 'POST':
        # 프론트엔드에서 전송한 데이터 받기
        store_name = request.POST.get('store_name')
        menu_name = request.POST.get('menu_name')
        quantity = request.POST.get('quantity')
        detail_name1 = request.POST.get('detail_name1')
        detail_name2 = request.POST.get('detail_name2')
        detail_name3 = request.POST.get('detail_name3')
        price = request.POST.get('price')

        # 가게 정보 저장
        store = Store.objects.create(name=store_name, latitude=0, longitude=0)

        # 메뉴 정보 저장
        menu = Menu.objects.create(
            name=menu_name,
            remaining_quantity=quantity,
            detail_name1=detail_name1,
            detail_name2=detail_name2,
            detail_name3=detail_name3,
            store=store
        )

        # 가격 정보 저장
        price = Price.objects.create(price=price, menu=menu)

        return render(request, 'store/add_store_menu.html', {'message': 'Store, Menu, and Price added successfully'})

    return render(request, 'store/add_store_menu.html')
