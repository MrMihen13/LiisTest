from rest_framework import serializers

from core.models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'  # TODO Change fields in ArticleEditSerializer


class AuthorRegistrationSerializer(serializers.ModelSerializer):
    ...  # TODO create AuthorRegistrationSerializer


class SubscriberRegistrationSerializer(serializers.ModelSerializer):
    ...  # TODO create SubscriberRegistrationSerializer
