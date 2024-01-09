# cart/views.py
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
        return Response({'detail': '장바구니가 비어 있습니다.'}, status=status.HTTP_200_OK)

    serializer = CartItemSerializer(cart_items, many=True)

    # 총 가격 계산
    total_price = sum(int(item['price']) for item in serializer.data)

    # 응답에 총 가격 추가
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
    store_name = request.data.get('store_name', "알 수 없는 가게")

    cart_item = CartItem.objects.create(user=user, product_name=product_name, price=price, store_name=store_name)
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
        raise Http404("장바구니에 항목이 없습니다.")

    cart_item.delete()
    return Response({'detail': '장바구니에서 항목이 제거되었습니다.'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def order(request):
    # 사용자의 access token로 사용자 식별
    user = request.user

    # 프론트엔드에서 전송한 데이터 받기
    product_name = request.data.get('product_name')
    store_name = request.data.get('store_name')
    price = request.data.get('price')

    # 주문 정보 저장
    Order.objects.create(user=user, product_name=product_name, store_name=store_name, price=price)

    return Response({'message': 'Order placed successfully'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_order_history(request):
    # 사용자의 access token로 사용자 식별
    user = request.user

    # 해당 사용자의 주문 내역 조회
    orders = Order.objects.filter(user=user)

    # 주문 내역을 직렬화하여 응답
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)