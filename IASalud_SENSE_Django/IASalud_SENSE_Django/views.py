from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.http import JsonResponse

from rest_framework_simplejwt.tokens import RefreshToken



def prueba1(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@api_view(['POST'])
def login(request):
    infoRequest = request.data
    user = get_object_or_404(User, username=infoRequest['usuario']['username'])
    if not user.check_password(infoRequest['usuario']['password']):
        return Response("Invalid Password")
    # token, created = Token.objects.get_or_create(user=user)
    token = RefreshToken.for_user(user)
    token["usuario"] = UserSerializer(user).data
    return Response({
                        'message': 'Logueado correctamente',
                        'refresh': str(token),
                        'access_token': str(token.access_token)
                    })

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()
        # Creacion del token para el usuario
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def pruebaToken(request):
    return Response({'message': 'Token valido', 'info': request.user.email}, status=status.HTTP_200_OK)

