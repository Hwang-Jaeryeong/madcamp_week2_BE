# star/views.py

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from .models import Store, Star


@require_POST
def post_star(request):
    try:
        # Try to parse the request body as JSON
        data = json.loads(request.body)
        store_name = data.get('store_name')
        rating_str = data.get('rating')
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON format.'}, status=400)

    # Check if 'store_name' and 'rating' parameters are provided
    if store_name is None or rating_str is None:
        return JsonResponse({'error': 'Both store_name and rating parameters are required.'}, status=400)

    # Check if 'rating' can be converted to int
    try:
        rating = int(rating_str)
    except ValueError:
        return JsonResponse({'error': 'Invalid rating value. Must be an integer.'}, status=400)

    store, created = Store.objects.get_or_create(name=store_name)
    user = request.user

    Star.objects.create(store=store, user=user, rating=rating)

    return JsonResponse({'message': 'Rating successfully added!'})


def get_average_rating(request):
    store_name = request.POST.get('store_name')
    store = get_object_or_404(Store, name=store_name)

    ratings = Star.objects.filter(store=store).values_list('rating', flat=True)

    if ratings:
        average_rating = sum(ratings) / len(ratings)
        return JsonResponse({'average_rating': average_rating})
    else:
        return JsonResponse({'message': 'No ratings available for this store.'})


