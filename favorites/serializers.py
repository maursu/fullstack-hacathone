from rest_framework import serializers

from . import models


class FavoritesSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = models.Favorites
        fields = '__all__'