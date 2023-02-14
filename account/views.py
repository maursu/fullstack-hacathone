from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework_simplejwt.views import TokenRefreshView
from drf_yasg.utils import swagger_auto_schema

from . import serializers as s
from . import permissions as p


User = get_user_model()

class RegistrationView(generics.CreateAPIView):
    serializer_class = s.RegistrationSerializer

    @swagger_auto_schema(request_body=s.RegistrationSerializer())
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return Response('Регистрация осуществлена')


class ActivationView(APIView):
    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code).first() #берем первого юзера
        if not user:
            return Response('Пользователь не найден', status=400)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('Активирован', status=200)


class LogoutView(APIView):
    permission_classes = [p.IsActivePermission]
    def post(self, request):
        return Response(
            'вы вышли со своего аккаунта'
        )


class ChangePasswordView(APIView):
    permission_classes = [p.IsActivePermission]

    @swagger_auto_schema(request_body=s.ChangePasswordSerializer)
    def post(self, request):
        serializer = s.ChangePasswordSerializer(
            data=request.data,
            context={'request':request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response('Пароль успешно обновлен', status=200)