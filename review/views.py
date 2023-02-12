from rest_framework import generics
from rest_framework.response import Response

from .serializers import AnswerReviewSerializer, QuestionReviewSerializer
from .models import AnswerReview, QuestionReview


class AnswerReviewListView(generics.ListAPIView):
    queryset = AnswerReview.objects.all()
    serializer_class = AnswerReviewSerializer


class QuestionReviewListView(generics.ListAPIView):
    queryset = QuestionReview.objects.all()
    serializer_class = QuestionReviewSerializer
