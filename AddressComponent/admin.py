from django.contrib import admin

# Register your models here.

from AddressComponent.models import State, Locality, Postcode, LocalPostalCode, Street, Address

admin.site.register(State)
admin.site.register(Locality)
admin.site.register(Postcode)
admin.site.register(LocalPostalCode)
admin.site.register(Street)
admin.site.register(Address)
