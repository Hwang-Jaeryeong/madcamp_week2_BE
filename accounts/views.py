# accounts/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.contrib.auth.hashers import make_password, check_password

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    data = request.data
    data['password'] = make_password(data['password'])  # 비밀번호를 해시화하여 저장
    serializer = CustomUserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = CustomUser.objects.filter(email=email).first()

    if user and check_password(password, user.password):
        refresh = RefreshToken.for_user(user)
        data = {
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
            'email': user.email,
            'username': user.username,
            'phone_number': user.phone_number,
            'current_location': user.current_location,
        }
        return Response(data, status=status.HTTP_200_OK)

    return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    # You can add additional logout logic here if needed
    return Response({'detail': 'Successfully logged out'}, status=status.HTTP_200_OK)

