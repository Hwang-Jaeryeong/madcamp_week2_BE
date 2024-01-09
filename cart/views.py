# views.py
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import CartItem
from .serializers import CartItemSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)

    if not cart_items:
        return Response({'detail': 'Your shopping cart is empty.'}, status=status.HTTP_200_OK)

    serializer = CartItemSerializer(cart_items, many=True)

    # Calculate total_price
    total_price = sum(int(item['price']) for item in serializer.data)

    # Add total_price to the response
    response_data = {
        'cart_items': serializer.data,
        'total_price': total_price
    }

    return Response(response_data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    user = request.user
    product_name = request.data.get('product_name')
    price = request.data.get('price')

    cart_item = CartItem.objects.create(user=user, product_name=product_name, price=price)
    serializer = CartItemSerializer(cart_item)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_cart(request, cart_item_order):
    cart_items = CartItem.objects.filter(user=request.user)

    # 순서로 정렬된 카트 아이템을 가져옵니다.
    sorted_cart_items = sorted(cart_items, key=lambda x: x.id)

    try:
        cart_item = sorted_cart_items[cart_item_order - 1]
    except IndexError:
        raise Http404("Item not found in the cart")

    cart_item.delete()
    return Response({'detail': 'Item removed from the cart'}, status=status.HTTP_204_NO_CONTENT)
