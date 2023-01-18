from django.urls import path
from .views import homePageView, ArticlsView, CreateArticls, ContentView, DeleteArticle, CreateView


urlpatterns = [
    path('', homePageView, name = 'home'),
    path('articls/', ArticlsView, name = 'articls'),
    path('articls/<int:id>/', ContentView, name = 'content_article'),
    path('articls/<int:id>/del/', DeleteArticle, name = 'delete_articls'),
    path('articls/new/',CreateView.as_view() , name = 'create_article'),
    
]