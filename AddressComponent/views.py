from AddressComponent.models import Address, Street, State
from AddressComponent.serializers import AddressSerializer, StreetSerializer, PostcodeSerializer, \
    LocalPostalCodeSerializer, LocalitySerializer, StateSerializer
from rest_framework import viewsets


# Address Component-Retrieving all address information by id
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
