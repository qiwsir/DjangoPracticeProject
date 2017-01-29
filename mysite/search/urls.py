from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^articles/$', views.search_articles, name="search_articles"),
    ]
