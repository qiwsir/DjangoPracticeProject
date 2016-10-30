from django.conf.urls import url
from . import views

from django.conf import settings

urlpatterns = [
    url(r'^$', views.user_login, name="user_login"),
#    url(r'(?P<article_id>\d)/$', views.blog_article, name="blog_detail"),
]
