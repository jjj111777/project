from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer # 회원가입
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


# 회원가입 기능 구현
class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "username": user.username,
                    "nickname": user.nickname,
                    "roles": [{"role": "USER"}],
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# 로그인 기능 추가
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({"token": str(refresh.access_token)})
        return Response({"error": "Invalid credentials"}, status=400)