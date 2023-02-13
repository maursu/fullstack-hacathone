from django.contrib.auth import get_user_model
from rest_framework import serializers

from .tasks import send_activation_code_celery

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=4, required=True, write_only=True)

    class Meta:
        model = User
        fields = [
            'password',
            'password_confirm', 
            'email',
            'username',
            
        ]

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm') #необходиом удалить из АТТРС. POPвозвращает и удаляет
        if password != password_confirm:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code_celery.delay(
            user.email, user.activation_code
        )
        return user

    