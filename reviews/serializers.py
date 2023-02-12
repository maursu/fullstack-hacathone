from rest_framework import serializers

from .models import AnswerReview, QuestionReview


class AnswerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerReview
        fields = '__all__'


class QuestionReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionReview
        fields = '__all__'
