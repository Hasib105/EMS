from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import UserRegistrationSerializer , EmployeeSerializer,AchievementEmployeeSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Employee,AchievementEmployee

# User Registration
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


# User Logout
class LogoutView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            refresh_token = self.request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            return token
        except KeyError:
            raise Http404('Refresh token not found')

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)



# List Employees
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]

class EmployeeCreateUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]



class AchievementEmployeeListView(generics.ListAPIView):
    queryset = AchievementEmployee.objects.all()
    serializer_class = AchievementEmployeeSerializer
    permission_classes = [AllowAny]