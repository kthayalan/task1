from django.urls import path, include
from AddressComponent.views import *

urlpatterns = [
    path('address/', AddressViewAPI.as_view(), name='address'),
]