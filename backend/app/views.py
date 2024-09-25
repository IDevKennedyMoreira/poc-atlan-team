# app/views.py
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import UserSerializer, RegisterSerializer

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'message': 'Login realizado com sucesso', 'user': UserSerializer(user).data})
    else:
        return Response({'error': 'Usuário ou senha incorretos'}, status=400)

@api_view(['POST'])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'message': 'Usuário registrado com sucesso', 'user': UserSerializer(user).data})
    return Response(serializer.errors, status=400)
