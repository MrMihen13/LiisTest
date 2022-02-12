from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

from core.models import Article, CustomUser
from core.utils.validators import custom_password_validator


class ArticleListSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.fullname')
    created_dt = serializers.CharField(source='create_datetime')

    class Meta:
        model = Article
        fields = ['title', 'description', 'body', 'image', 'author_name', 'created_dt']


class ArticleEditSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.fullname', read_only=True)

    class Meta:
        model = Article
        fields = ['title', 'description', 'body', 'image', 'is_open', 'author']

    def create(self, validated_data, **kwargs):
        title = validated_data['title']
        description = validated_data['description']
        body = validated_data['body']
        image = validated_data['image']
        is_open = validated_data['is_open']
        author = kwargs['author']

        article = self.Meta.model.objects.create(
            title=title, description=description, body=body, image=image, is_open=is_open, author=author)

        return article


class AuthorRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=8, label='Password', style={'input_type': 'password'},
        validators=[validate_password, custom_password_validator], required=False, write_only=True)
    password2 = serializers.CharField(label='Repeat password', style={'input_type': 'password'}, required=False, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'avatar', 'password', 'password2']

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
        validators=[validate_password, custom_password_validator], required=False, write_only=True)
    password2 = serializers.CharField(label='Repeat password', style={'input_type': 'password'}, required=False, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'avatar', 'password', 'password2']

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
