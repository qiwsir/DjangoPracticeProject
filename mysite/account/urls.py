from django.conf.urls import url
from . import views

from django.conf import settings

urlpatterns = [
    url(r'^$', views.register, name="register_user"),
#    url(r'(?P<article_id>\d)/$', views.blog_article, name="blog_detail"),
]
