from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),  
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('logout/', views.LogoutView.as_view(), name='logout'), 
    # path('me/', UserDetailView.as_view(), name='user_detail'),  

]
