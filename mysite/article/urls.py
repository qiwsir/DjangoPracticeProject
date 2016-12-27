from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list-article/$', views.articles_list, name="articles_list"),
    ] 