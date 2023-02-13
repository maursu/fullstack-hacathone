from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema

from .serializers import RegistrationSerializer


User = get_user_model()

class RegistrationView(generics.CreateAPIView):
    @swagger_auto_schema(request_body=RegistrationSerializer())
    def post(self, request):
        data = request.data #получить JSON
        print(data)
        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Регистрация осуществлена', status=201)


class ActivationView(APIView):
    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code).first() #берем первого юзера
        if not user:
            return Response('Пользователь не найден', status=400)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('Активирован', status=200)


# class LoginView(ObtainAuthToken):
#     serializer_class = LoginSerializer

# class LogoutView(APIView):
#     permission_classes = [IsActivePermission]
#     def post(self, request):
#         user = request.user
#         Token.objects.filter(user=user).delete()
#         return Response(
#             'вы вышли со своего аккайнта'
#         )


# class ChangePasswordView(APIView):
#     permission_classes = [IsAuthenticated]
#     @swagger_auto_schema(request_body=ChangePasswordSerializer)
#     def post(self, request):
#         serializer = ChangePasswordSerializer(
#             data=request.data,
#             context={'request':request}
#         )
#         if serializer.is_valid(raise_exception=True):
#             serializer.set_new_password()
#             return Response('Пароль успешно обновлен', status=200)


# class ForgotPasswordView(APIView):
#     @swagger_auto_schema(request_body=ForgotPasswordSerializer)
#     def post(self, request):
#         serializer = ForgotPasswordSerializer(
#             data = request.data
#         )
#         if serializer.is_valid(raise_exception=True):
#             serializer.send_verification_email()
#             return Response(
#                     'Вам выслали сообщение для восстановления пароля'
                
#                 )

# class ForgotPasswordCompleteView(APIView):
#     @swagger_auto_schema(request_body=ForgotPasswordCompleteSerializer)
#     def post(self,request):
#         serializer = ForgotPasswordCompleteSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.set_new_password()
#             return Response(
#                 'Ваш пароль успешно восстановлен'
#                 )
