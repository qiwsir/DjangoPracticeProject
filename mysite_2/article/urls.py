from django.urls import path, re_path
from . import views, list_views

app_name = "article"

urlpatterns = [
    path('article-column/', views.article_column, name="article_column"),
    path('rename-column/', views.rename_article_column, name="rename_article_column"),
    path('del-column/', views.del_article_column, name="del_article_column"),
    path('article-post/', views.article_post, name="article_post"),
    path('article-list/', views.article_list, name="article_list"),
    re_path('article-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.article_detail, name="article_detail"),
    path('del-article/', views.del_article, name="del_article"),
    path('redit-article/<int:article_id>/', views.redit_article, name="redit_article"),

    path('list-article-titles/', list_views.article_titles, name="article_titles"),
    path('article-content/<int:id>/<slug:slug>/', list_views.article_detail, name="article_content"),
    path('list-article-titles/<username>/', list_views.article_titles, name="author_articles"),
    path('like-article/', list_views.like_article, name="like_article"),

    path('article-tag/', views.article_tag, name="article_tag"),
    path('del-article-tag/', views.del_article_tag, name="del_article_tag"),
]
