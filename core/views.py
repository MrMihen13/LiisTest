from rest_framework import generics, permissions, response, status

from core.models import Article, CustomUser
from core.serializers import (
    ArticleListSerializer, ArticleEditSerializer, AuthorRegistrationSerializer, SubscriberRegistrationSerializer,
)
from core.permissions import IsAuthorUser, IsSubscriberUser, IsOwnerOrReadOnly


class ArticleListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ArticleListSerializer
    queryset = Article.objects.all()

    def get(self, request, *args, **kwargs):

        articles = self.get_queryset()

        print(request.user.is_authenticated)

        if request.user.is_authenticated and request.user.role == 'subscriber':

            serializer = self.serializer_class(articles, many=True)

            return response.Response(data=serializer.data, status=status.HTTP_200_OK)

        else:

            articles = articles.filter(is_open=True)
            serializer = self.serializer_class(articles, many=True)

            return response.Response(data=serializer.data, status=status.HTTP_200_OK)


class ArticleView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ArticleListSerializer
    queryset = Article.objects.all()

    def get(self, request, pk, *args, **kwargs):

        articles = self.get_queryset()
        articles = articles.filter(id=pk)

        if request.user.is_authenticated and request.user.role == 'subscriber':

            serializer = self.serializer_class(articles, many=True)

            return response.Response(data=serializer.data, status=status.HTTP_200_OK)

        else:

            articles = articles.filter(is_open=True)
            serializer = self.serializer_class(articles, many=True)

            return response.Response(data=serializer.data, status=status.HTTP_200_OK)


class ArticleEditApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly, IsAuthorUser)
    serializer_class = ArticleEditSerializer
    queryset = Article.objects.all()


class ArticleCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsAuthorUser)
    serializer_class = ArticleEditSerializer
    queryset = Article.objects.all()

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.create(serializer.validated_data, author=request.user)

        return response.Response(data=serializer.data, status=status.HTTP_200_OK)


class AuthorRegistrationView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = AuthorRegistrationSerializer
    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return response.Response(serializer.data, status=status.HTTP_200_OK)


class SubscriberRegistrationView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SubscriberRegistrationSerializer
    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return response.Response(serializer.data, status=status.HTTP_200_OK)
