from django.urls import path, include
from Authentication.views import LoginAPI, get_data, UserAddressViewAPI

urlpatterns = [
    path('login/', LoginAPI.as_view()),
    path('user_data/', get_data),
    path('user_address/<int:id>/', UserAddressViewAPI.as_view(), name='user_address')
]