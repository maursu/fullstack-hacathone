from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from .models import Tag, Question
from favorites.models import Favorites
from .permissions import IsOwnerOrReadOnly, IsAdminAuthPermission
from . import serializers


class PermissionsMixin():
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = [AllowAny]
        elif self.action == 'create':
            permissions = [IsAdminAuthPermission]
        elif self.action in ['update','partial_update', 'destroy']:
            permissions = [IsAdminUser, IsOwnerOrReadOnly] 
        else:
            permissions = [IsAdminAuthPermission]
        return [permission() for permission in permissions]


class TagViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class QuestionViewSet(PermissionsMixin, ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tag']

    def list(self, request, *args, **kwargs):
        self.serializer_class = serializers.QuestionListSerializer
        return super().list(request, *args, **kwargs)

    @action(['POST'], detail=True)
    def favorite(self,request,pk):
        question = self.get_object()
        user = request.user
        try:
            favorite = Favorites.objects.get(question=question, user=user)
            favorite.is_favorite = not favorite.is_favorite
            favorite.save()
            message = 'Added to favorites' if favorite.is_favorite else 'Removed from favorites'
            if not favorite.is_favorite:
                favorite.delete()
        except Favorites.DoesNotExist:
            Favorites.objects.create(question=question, user=user, is_favorite=True)
            message = 'Added to favorite'
        return Response(message, status=200)