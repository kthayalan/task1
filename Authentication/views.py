from functools import partial
from urllib import response
from xmlrpc.client import ResponseError
from django.shortcuts import render
from Authentication.serializers import LoginSerializer, HomeSerializer, UserRetrievalSerializer, StateSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from Authentication.models import User
from rest_framework import generics


# User login and JWT generation
class LoginAPI(APIView):

    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)

        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']

            user = authenticate(username=username, password=password)

            if user is None:
                return Response({'message': 'Username or password incorrect'})
            else:
                refresh = RefreshToken.for_user(user)

                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
        else:
            return Response(
                {
                    'message': serializer.errors
                }
            )


# User Authentication for get data
@api_view(http_method_names=['GET'])
@permission_classes([IsAuthenticated])
def get_data(request):
    user = request.user
    return Response({
        'user_info': {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
    })


# User address retrieval and edit
class UserAddressViewAPI(APIView):
    def get(self, request, id: int):
        count_users = User.objects.count()
        if id <= count_users:
            queryset = User.objects.get(id=id)
            serializer = UserRetrievalSerializer(queryset)
            return Response(serializer.data)
        else:
            return Response({'Message': 'invalid user id'})

    def patch(self, request, id: int):
        count_users = User.objects.count()
        if id <= count_users:
            data = request.data
            queryset = User.objects.get(id=id)
            serializer = UserRetrievalSerializer(instance=queryset, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'Address updated': serializer.data})
            else:
                return Response(serializer.errors)
        else:
            return Response({'Message': 'invalid user id'})
