from rest_framework import generics, permissions

from core.models import Article
from core.serializers import (
    ArticleListSerializer, ArticleEditSerializer, AuthorRegistrationSerializer, SubscriberRegistrationSerializer,
)
from core.permissions import IsAuthorUser, IsSubscriberUser, IsOwnerOrReadOnly


class ArticleCreateView(generics.ListCreateAPIView):
    serializer_class = ArticleEditSerializer
    permission_classes = (permissions.IsAuthenticated, IsAuthorUser)
    queryset = Article.objects.all()


class ArticleListView(generics.ListAPIView):
    permissions = (permissions.IsAuthenticated, IsSubscriberUser)
    serializer_class = ArticleListSerializer
    queryset = Article.objects.all()  # TODO Create different queryset for different role


class ArticleEditApiView(generics.RetrieveUpdateDestroyAPIView):
    permissions = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = ArticleEditSerializer
    queryset = Article.objects.all()


class RegistrationAuthorView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ...  # TODO create serializer for registration Author

    def post(self, request, *args, **kwargs):
        ...  # TODO create logic fot registration Author


class RegistrationSubscriberView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ...  # TODO create serializer for registration Subscriber

    def post(self, request, *args, **kwargs):
        ...  # TODO create logic fot registration Subscriber
