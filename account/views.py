from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics

from .serializers import RegistrationSerializer


User = get_user_model()

class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

