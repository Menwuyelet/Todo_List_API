from django.urls import path
from .views import RegistrationView, LogoutView, DeleteUserView, UpdateProfileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name = 'login'),
    path('refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
    path('register/', RegistrationView.as_view(), name = 'signup'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('delete/', DeleteUserView.as_view(), name = 'delete_user'),
    path('update/', UpdateProfileView.as_view(), name = 'update_profile'),
]