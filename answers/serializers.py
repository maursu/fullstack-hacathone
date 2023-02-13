from rest_framework import serializers

from .models import Answer, Comment


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'author.username')

    class Meta:
        model = Answer
        fields = '__all__'

    def create(self,validated_data):
        request = self.context.get('request')
        user = request.user
        answer = Answer.objects.create(author=user, **validated_data)
        return answer

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['comments'] = CommentSerializer(Comment.objects.filter(answer=instance.pk), many=True).data
        return representation


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'author.username')

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self,validated_data):
        request = self.context.get('request')
        user = request.user
        comment = Comment.objects.create(author=user, **validated_data)
        return comment