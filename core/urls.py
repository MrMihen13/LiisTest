from django.urls import path

from core import views


urlpatterns = [
    path('articles', views.ArticleListView.as_view()),
    path('article/<int:pk>', views.ArticleView.as_view()),
    path('article/edit/<int:pk>', views.ArticleEditApiView.as_view()),
    path('article/create', views.ArticleCreateView.as_view()),
    path('author/register', views.AuthorRegistrationView.as_view()),
    path('registration', views.SubscriberRegistrationView.as_view())
]
