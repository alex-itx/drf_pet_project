from rest_framework import serializers

from .models import Women

# Сериализатор для таблицы women
class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ['title', 'cat_id']