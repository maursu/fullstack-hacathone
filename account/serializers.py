from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import serializers


from .tasks import send_activation_code_celery

User = get_user_model()
email = ''

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


class ChangePasswordSerializer(
    serializers.ModelSerializer):
    old_password = serializers.CharField(
        min_length=4, required=True
    )
    new_password = serializers.CharField(
        min_length=4, required=True
    )
    new_password_confirm = serializers.CharField(
        min_length=4, required=True
    )

    class Meta:
        model = User
        fields = ['old_password', 'new_password', 'new_password_confirm']
    
    def validate_old_password(self, old_pass):
        request = self.context.get('request')
        user = request.user

        if not user.check_password(old_pass):
            raise serializers.ValidationError(
                'Введите корректный пароль'
            )
        return old_pass
    
    def validate(self, attrs):
        new_pass = attrs.get('new_password')
        new_pass_confirm = attrs.pop('new_password_confirm')
        if new_pass != new_pass_confirm:
            raise serializers.ValidationError(
                'Пароли не совпадают'
            )
        return attrs

    def set_new_password(self):
        new_pass = self.validated_data.get(
            'new_password'
        )
        user = self.context['request'].user
        user.set_password(new_pass)
        user.save()