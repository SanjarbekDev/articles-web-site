from django.urls import path
from .views import homePageView, ArticlsView, CreateArticls, ContentView, DeleteArticle, add


urlpatterns = [
    path('', homePageView, name = 'home'),
    path('articls/', ArticlsView, name = 'articls'),
    path('articls/<int:id>/', ContentView, name = 'content_article'),
    path('articls/<int:id>/del/', DeleteArticle, name = 'delete_articls'),
    path('articls/new/',CreateArticls , name = 'create_article'),
    path('articls/new/add/',add , name = 'add'),
    
]