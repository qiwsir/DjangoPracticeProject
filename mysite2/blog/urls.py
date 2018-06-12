from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_title),
    path('<int:article_id>/', views.blog_article),
]
