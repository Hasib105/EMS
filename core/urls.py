from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    #Authentication
    path('register/', views.UserRegistrationView.as_view(), name='register'),  
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('logout/', views.LogoutView.as_view(), name='logout'), 

    #Employees Crud
    path('employees/', views.EmployeeListCreateView.as_view(), name='employee-list'),  # List all employees
    path('employees/<int:pk>/', views.EmployeeCreateUpdateView.as_view(), name='employee-detail'),  # Retrieve, update, delete a specific employee
    path('achievements/', views.AchievementEmployeeListView.as_view(), name='achievement-employee-list'),  # List all AchievementEmployee records

]
