from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import serializers


from .tasks import send_activation_code_celery

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=4, required=True, write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'password',
            'password_confirm',
            'email',
            'username',
            'name',
            'user_photo',
            'last_name',
            'github_account',
            'telegram_account',
            'web_site',  
        ]

    def validate_github_account(self, github_link):
        if not github_link.startswith('www.github.com/') and not github_link.startswith('https://github.com/'):
            raise serializers.ValidationError(
                'некоррекнтная ссылка на гитхаб, введите в формате www.github.com/username или https://github.com/  '
            )
        return github_link
    
    def validate_telegram_account(self, telegramm_link):
        if not telegramm_link.startswith('https://t.me/'):
            raise serializers.ValidationError(
                'некорректная ссылка на телеграм, введите в формате https://t.me/username'
            )
        return telegramm_link


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


class ChangePasswordSerializer(serializers.ModelSerializer):
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
        fields = [
            'old_password',
            'new_password',
            'new_password_confirm'
        ]
    
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


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                'Такого пользователя не зарегистрировано'
            )
        return email
    
    def send_verification_email(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.create_activation_code()
        send_mail(
            'Восстановление пароля',
            f'Ваш код восстановления: {user.activation_code}',
            'example@gmail.com',
            [user.email]
        )


class ForgotPasswordCompleteSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=4, required=True)
    password_confirm = serializers.CharField(min_length=4, required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        code = attrs.get('code')
        password1 = attrs.get('password')
        password2 = attrs.get('password_confirm')
    
        if not User.objects.filter(email=email, activation_code=code).exists():
            raise serializers.ValidationError(
                'Пользователь не найден или введен неправильный код'
            )
    
        if password1!=password2:
            raise serializers.ValidationError(
                'Пароли не совпадают'
            )
        return attrs

    def set_new_password(self):
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')
        user = User.objects.get(email=email)
        user.set_password(password)
        user.activation_code = ''
        user.save()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'name',
            'last_name',
            'user_photo',
            'github_account',
            'telegram_account',
            'web_site',
            'id',
        ]




    