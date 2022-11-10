from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from Authentication.models import User
from AddressComponent.models import *


# from AddressComponent.serializers import *

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phoneNo']


# Serializers for retriving user address
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['country']


class LocalitySerializer(serializers.ModelSerializer):
    state = StateSerializer(many=False, read_only=False)

    class Meta:
        model = Locality
        fields = [field.name for field in model._meta.fields]


class PostcodeSerializer(serializers.ModelSerializer):
    state = StateSerializer(many=False, read_only=False)

    class Meta:
        model = Postcode
        fields = [field.name for field in model._meta.fields]


class LocalPostalCodeSerializer(serializers.ModelSerializer):
    locality = LocalitySerializer(many=False, read_only=False)

    class Meta:
        model = LocalPostalCode
        fields = ['name', 'locality']


class StreetSerializer(serializers.ModelSerializer):
    # local_postal_code = LocalPostalCodeSerializer(many=False, read_only=True)

    class Meta:
        model = Street
        fields = ['name']


class AddressSerializer(serializers.ModelSerializer):
    street = StreetSerializer(many=False, read_only=False)
    country = serializers.SerializerMethodField()

    class Meta:
        model = Address
        fields = ['no', 'address_1', 'street', 'country']

    def get_country(self, obj):
        return obj.street.local_postal_code.locality.state.country


class UserRetrievalSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False, read_only=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'address']

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address')
        address = instance.address

        street_data = address_data.pop('street')
        street = instance.address.street

        address.no = address_data.get('no', address.no)
        address.address_1 = address_data.get('address_1', address.address_1)
        address.save()

        street.name = street_data.get('name', street.name)
        street.save()

        return instance
