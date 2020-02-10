from django.urls import path, include
from .views import (
    user_login,
    user_registration,
    
)


urlpatterns = [

    path('register/', user_registration.UserRegistration.as_view(), name='user_registration'),
    path('login/', user_login.UserLogin.as_view(), name='user_login' ),
]
