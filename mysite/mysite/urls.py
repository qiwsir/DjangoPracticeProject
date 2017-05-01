"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.flatpages import views
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include("blog.urls", namespace="blog", app_name="blog")),
    url(r'^account/', include("account.urls", namespace='account', app_name='account')),
    url(r'^pwd_reset/', include("password_reset.urls", namespace='pwd_reset', app_name='pwd_reset')),
    url(r'^article/', include('article.urls', namespace='article', app_name='article')),
    url(r'^home/', TemplateView.as_view(template_name="home.html"), name="home"),
    url(r'^image/', include('image.urls', namespace='image', app_name='image')),
    url(r'^course/', include('course.urls', namespace='course', app_name='course')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
