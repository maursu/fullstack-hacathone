from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import AnswerReviewSerializer, QuestionReviewSerializer, CommentReviewSerializer
from .models import AnswerReview, QuestionReview, CommentReview
from answers.models import Answer
from questions.models import Question
from answers.models import Comment


class AnswerReviewListView(generics.ListAPIView):
    queryset = AnswerReview.objects.all()
    serializer_class = AnswerReviewSerializer


@api_view(['POST'])
def answer_like(request, pk=None):
    answer = Answer.objects.get(pk=pk)
    author = request.user
    serializer = AnswerReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        try:
            answer_review = AnswerReview.objects.get(
                answer=answer, author=author)
            answer_review.delete()
            message = 'disliked'
        except AnswerReview.DoesNotExist:
            AnswerReview.objects.create(answer=answer, author=author)
            message = 'liked'
        return Response(message, status=200)


class QuestionReviewListView(generics.ListAPIView):
    queryset = QuestionReview.objects.all()
    serializer_class = QuestionReviewSerializer


@api_view(['POST'])
def question_like(request, slug=None):
    question = Question.objects.get(slug=slug)
    author = request.user
    serializer = QuestionReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        try:
            question_review = QuestionReview.objects.get(
                question=question, author=author)
            question_review.delete()
            message = 'disliked'
        except QuestionReview.DoesNotExist:
            QuestionReview.objects.create(question=question, author=author)
            message = 'liked'
        return Response(message, status=200)


class CommentReviewListView(generics.ListAPIView):
    queryset = CommentReview.objects.all()
    serializer_class = CommentReviewSerializer


@api_view(['POST'])
def comment_like(request, pk=None):
    comment = Comment.objects.get(pk=pk)
    author = request.user
    serializer = CommentReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        try:
            comment_review = CommentReview.objects.get(
                comment=comment, author=author)
            comment_review.delete()
            message = 'disliked'
        except CommentReview.DoesNotExist:
            CommentReview.objects.create(comment=comment, author=author)
            message = 'liked'
        return Response(message, status=200)
