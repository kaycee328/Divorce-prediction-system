from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication
from .serializers import CreateUserSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]  # Basic Authentication for API


class LoginView(APIView):
    def post(self, request, format=None):
        username = request.data.get("username")
        print(username)
        password = request.data.get("password")
        print(password)
        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user_id": user.id,
                    "username": user.username,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST
        )


class Test(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {"message": "This is a protected endpoint."}
        return Response(data, status=status.HTTP_200_OK)
