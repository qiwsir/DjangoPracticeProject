from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path('article-column/', views.article_column, name="article_column"), 
    path('rename-column/', views.rename_article_column, name="rename_article_column"),
    path('del-column/', views.del_article_column, name="del_article_column"),
]