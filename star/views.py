# star/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import StoreRating
from django.db.models import Avg

@csrf_exempt  # CSRF 보호 해제 (테스트용이므로 나중에 적절한 보안을 위해 수정할 것)
def add_store_rating(request):
    if request.method == 'POST':
        try:
            store_name = request.POST['store_name']
            rating = request.POST['rating']
        except KeyError:
            return JsonResponse({'error': '가게 이름과 별점을 모두 입력하세요.'}, status=400)

        if store_name and rating:
            StoreRating.objects.create(store_name=store_name, rating=rating)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': '가게 이름과 별점을 모두 입력하세요.'}, status=400)
    else:
        return JsonResponse({'error': 'POST 메서드만 지원됩니다.'}, status=405)

@csrf_exempt
def get_store_average_rating(request):
    if request.method == 'GET':
        try:
            store_name = request.GET['store_name']
        except KeyError:
            return JsonResponse({'error': '가게 이름을 입력하세요.'}, status=400)

        if store_name:
            average_rating = StoreRating.objects.filter(store_name=store_name).aggregate(Avg('rating'))['rating__avg']
            if average_rating is not None:
                return JsonResponse({'average_rating': average_rating})
            else:
                return JsonResponse({'error': '가게에 등록된 평점이 없습니다.'}, status=404)
        else:
            return JsonResponse({'error': '가게 이름을 입력하세요.'}, status=400)
    else:
        return JsonResponse({'error': 'GET 메서드만 지원됩니다.'}, status=405)

