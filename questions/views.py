from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .models import Tag, Question
from .serializers import TagSerializer, QuestionSerializer


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
