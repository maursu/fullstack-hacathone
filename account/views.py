from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema

from .serializers import RegistrationSerializer


User = get_user_model()

class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

    @swagger_auto_schema(request_body=RegistrationSerializer)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


# class ActivationView(APIView):
#     @swagger_auto_schema(request_body=ActivationSerializer)
#     def post(self, request):
#         serializer = ActivationSerializer(
#             data=request.data)
#         serializer.is_valid(
#             raise_exception=True)
#         serializer.activate()
#         return Response(
#             'Аккаунт успешно активирован', status=200
#         )


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
