from difflib import SequenceMatcher

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny
import django_filters
from rest_framework import filters
from fuzzywuzzy import fuzz

from .models import Tag, Question
from favorites.models import Favorites
from .permissions import IsOwnerOrReadOnly, IsAdminAuthPermission
from . import serializers
from parser.utils import parser
from parser.serializers import StackOverflowSerialiser


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
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['tag']
    search_fields = ['tag', 'title']
    ordering_fields = ['title', 'views_count', 'updated_at', 'created_at']
    ordering = ['created_at']

    def list(self, request, *args, **kwargs):
        self.serializer_class = serializers.QuestionListSerializer
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        question = self.get_object()
        question.views_count += 1
        question.save()
        serializer = self.get_serializer(question)
        return Response(serializer.data)
    
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

    @action(['POST'], detail=True)
    def similar_questions(self, request, pk):
        question = self.get_object()
        title = question.title
        queryset = Question.objects.all()
        matches = []
        for i in queryset:
            result = SequenceMatcher(None, title, i.title).ratio()
            if result > 0.7:
                matches.append(i)
        if matches != []:
            serializer = serializers.QuestionSerializer(matches, many=True)
            return Response(serializer.data, status=200)
        else:
            return Response("Sorry. Matches didn't find")
    
    @action(['POST'], detail=True)
    def find_on_stackoverflow(self, request, pk):
        question = self.get_object()
        title = question.title
        tag = question.tag.all()[0]
        parsed_list = parser(tag)
        matches = []
        for i in parsed_list:
            result = fuzz.WRatio(title.lower(), i[0].lower())
            if result > 90:
                matches.append({'title':i[0], 'link':[i[1]]})
        if matches != []:
            serializer = StackOverflowSerialiser(matches, many=True)
            return Response(serializer.data, status=200)
        else:
            return Response("Sorry. We didn't find similar questions on Stackoverflow.")