# views.py
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
    total_price = sum(float(item['price']) for item in serializer.data)

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
def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.filter(id=cart_item_id, user=request.user).first()
    if cart_item:
        cart_item.delete()
        return Response({'detail': 'Item removed from the cart'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'detail': 'Item not found in the cart'}, status=status.HTTP_404_NOT_FOUND)
