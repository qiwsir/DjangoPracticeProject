from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list-article/$', views.list_articles, name="list_articles"),
    url(r'^read-article/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.read_article, name="read_article"),
    ] 