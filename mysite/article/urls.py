from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list-article/$', views.list_articles, name="list_articles"),
    url(r'^read-article/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.read_article, name="read_article"),
    url(r'^list-article/(?P<username>[-\w]+)/$', views.list_articles, name="author_articles"),
    url(r'^like-article/$', views.like_article, name="like_article"),
    ] 