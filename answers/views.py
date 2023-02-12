from rest_framework.viewsets import ModelViewSet

from .serializers import AnswerSerializer
from .models import Answer


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer