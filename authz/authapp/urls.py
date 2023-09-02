
from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('user_data/', views.fetch_userdata),
    path('jwt_token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt_token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
