from dataclasses import field, fields
from rest_framework import serializers

from AddressComponent.models import Address, Street, LocalPostalCode, Postcode, Locality, State
ADDRESSSER = {}

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = [field.name for field in model._meta.fields]

ADDRESSSER[State._meta.model_name] = StateSerializer

class LocalitySerializer(serializers.ModelSerializer):
    state = ADDRESSSER[State._meta.model_name](many=False, read_only=True)
    class Meta:
        model = Locality
        fields = [field.name for field in model._meta.fields]

ADDRESSSER[Locality._meta.model_name] = LocalitySerializer

class PostcodeSerializer(serializers.ModelSerializer):
    state = ADDRESSSER[State._meta.model_name](many=False, read_only=True)
    class Meta:
        model = Postcode
        fields = [field.name for field in model._meta.fields]
ADDRESSSER[Postcode._meta.model_name] = PostcodeSerializer


class LocalPostalCodeSerializer(serializers.ModelSerializer):
    locality = ADDRESSSER[Locality._meta.model_name](many=False, read_only=True)
    class Meta:
        model = LocalPostalCode
        fields = [field.name for field in model._meta.fields]
ADDRESSSER[LocalPostalCode._meta.model_name] = LocalPostalCodeSerializer


class StreetSerializer(serializers.ModelSerializer):
    local_postal_code = ADDRESSSER[LocalPostalCode._meta.model_name](many=False, read_only=True)
    class Meta:
        model = Street
        fields = [field.name for field in model._meta.fields]
ADDRESSSER[Street._meta.model_name] = StreetSerializer

class AddressSerializer(serializers.ModelSerializer):
    street = ADDRESSSER[Street._meta.model_name](many=False, read_only=True)
    class Meta:
        model = Address
        fields = [field.name for field in model._meta.fields]

ADDRESSSER[Address._meta.model_name] = AddressSerializer