from django.urls import path
from .views import RegisterView, LoginView, VerifyEmail, api_detail_user_view, api_update_user_view
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token



urlpatterns = [
    path('register-api/', RegisterView.as_view(), name='register-api'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
    path('login-api/', LoginView.as_view(), name='login-api'),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('<id>/', api_detail_user_view, name="user_detail"),
    path('<id>/update/', api_update_user_view, name="user_update"),
]
