from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import RegisterUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
]
