# store/views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from .models import Store, Menu, Price, Star

def store_list(request):
    stores = Store.objects.all()
    store_dict = {store.name: store.id for store in stores}
    return JsonResponse(store_dict)

def store_detail(request, store_id, menu_id=None):
    if menu_id is not None:
        menu = get_object_or_404(Menu, store_id=store_id, id=menu_id)
        response_data = menu.as_dict()
    else:
        menus = Menu.objects.filter(store_id=store_id)
        store_name = get_object_or_404(Store, id=store_id).name
        menu_list = [
            {
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
            "menus": menu_list
        }

    return JsonResponse(response_data)

def menu_price(request, store_id, menu_id):
    try:
        price = Price.objects.get(menu_id=menu_id)
    except Price.DoesNotExist:
        return JsonResponse({"error": "가격을 찾을 수 없습니다."}, status=404)

    return JsonResponse({"가격": price.price})


@require_POST
def rate_store(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    rating = int(request.POST.get('rating', 0))

    if 1 <= rating <= 5:
        Star.objects.create(store=store, rating=rating)

    return JsonResponse({'message': 'Rating submitted successfully'})


@require_GET
def get_average_rating(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    ratings = Star.objects.filter(store=store).values_list('rating', flat=True)

    if ratings:
        average_rating = sum(ratings) / len(ratings)
    else:
        average_rating = 0

    return JsonResponse({'average_rating': average_rating})
