from rest_framework import serializers

from .models import Tag, Question
from review.models import Answer
from review.serializers import AnswerSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title',)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['answers'] = AnswerSerializer(Answer.objects.filter(question=instance.pk), many=True).data
        return representation
