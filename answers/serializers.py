from rest_framework import serializers

from .models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

    # def create(self,validated_data):
    #     request = self.context.get('request')
    #     user = request.user
    #     answer = Answer.objects.create(author=user, **validated_data)
    #     return answer
