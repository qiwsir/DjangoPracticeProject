from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_title, name='blog_title'),
    #path('<int:article_id>/', views.blog_article),
    path('<int:article_id>/', views.blog_article, name='blog_article'),
]