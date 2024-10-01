from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import UserRegistrationSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]



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

