from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from AddressComponent.models import Address, Street, State
from AddressComponent.serializers import AddressSerializer, StreetSerializer, PostcodeSerializer, LocalPostalCodeSerializer, LocalitySerializer, StateSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


# Address Component-Retriving all address information by id
class AddressViewAPI(APIView):

    def get(self, request):
        id = request.GET.get('id')
        queryset = Address.objects.all()

        if id:
            queryset = queryset.filter(id=id)

        else:
            return Response({'Message': 'Id is empty'})

        serializer = AddressSerializer(queryset, many=True)

        return Response({
            'Address': serializer.data
        })

    