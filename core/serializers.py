from django.contrib.auth.password_validation import get_password_validators

from rest_framework import serializers

from core.models import Article, CustomUser
from core.utils.validators import password_validator


class ArticleListSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.fullname')
    created_dt = serializers.CharField(source='create_datetime')

    class Meta:
        model = Article
        fields = ['title', 'description', 'body', 'author_name', 'created_dt', 'image']


class ArticleEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'description', 'body', 'image']


class AuthorRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=8, label='Password', style={'input_type': 'password'},
        validators=[get_password_validators, password_validator], required=False, write_only=True)
    password2 = serializers.CharField(min_length=8, label='Repeat password', style={'input_type': 'password'}, required=False, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'password2']

    def create(self, validated_data):
        password = validated_data['password']
        password2 = validated_data['password2']
        email = validated_data['email']

        if password != password2:
            raise serializers.ValidationError('Passwords do not match')

        author = self.Meta.model.objects.create(email=email, role='author')
        author.set_password(raw_password=password)
        author.save()

        return author


class SubscriberRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=8, label='Password', style={'input_type': 'password'},
        validators=[get_password_validators, password_validator], required=False, write_only=True)
    password2 = serializers.CharField(min_length=8, label='Repeat password', style={'input_type': 'password'}, required=False, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'password2']

    def create(self, validated_data):
        password = validated_data['password']
        password2 = validated_data['password2']
        email = validated_data['email']

        if password != password2:
            raise serializers.ValidationError('Passwords do not match')

        sub = self.Meta.model.objects.create(email=email, role='subscriber')
        sub.set_password(raw_password=password)
        sub.save()

        return sub
