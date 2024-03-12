from django.urls import path
from .views import logout, registration, get_user
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = 'user'
urlpatterns = [
    path('registration/', registration, name='registration'),
    path('logout/', logout, name='logout'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<str:pk>/', get_user, name='get_user'),
]