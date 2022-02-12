from rest_framework import generics, permissions, response, status

from core.models import Article, CustomUser
from core.serializers import (
    ArticleListSerializer, ArticleEditSerializer, AuthorRegistrationSerializer, SubscriberRegistrationSerializer,
)
from core.permissions import IsAuthorUser, IsSubscriberUser, IsOwnerOrReadOnly


class ArticleCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsAuthorUser)
    serializer_class = ArticleEditSerializer
    queryset = Article.objects.all()


class ClosedArticleListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, IsSubscriberUser)
    serializer_class = ArticleListSerializer
    queryset = Article.objects.filter(is_open=False)


class ArticleListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ArticleListSerializer
    queryset = Article.objects.all()


class OpenArticleListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, IsSubscriberUser)
    serializer_class = ArticleListSerializer
    queryset = Article.objects.filter(is_open=True)


class ArticleEditApiView(generics.RetrieveUpdateDestroyAPIView):
    permissions = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = ArticleEditSerializer
    queryset = Article.objects.all()


class AuthorRegistrationView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = AuthorRegistrationSerializer
    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return response.Response(serializer.data)


class SubscriberRegistrationView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SubscriberRegistrationSerializer
    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return response.Response(serializer.data)
