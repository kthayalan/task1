from django.urls import path, include
from AddressComponent.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'address', AddressViewSet)

urlpatterns = [
    path('', include(router.urls))
]