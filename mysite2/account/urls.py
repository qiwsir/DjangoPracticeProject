from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

app_name = "account"

urlpatterns = [
    #path('login/', views.user_login, name='user_login'),
    path('login/', auth_views.login, name='user_login'),
    path('new-login/', auth_views.login, {'template_name': 'account/login.html'}, name='user_login'),
    path('logout/', auth_views.logout, {'template_name': 'account/logout.html'}, name='user_logout'),
    path('register/', views.register, name='user_register'),
    path('password-change/', auth_views.password_change, {"post_change_redirect":"/account/password-change-done", 'template_name': 'account/password_change_form.html'}, name='password_change'),
    path('password-change-done/', auth_views.password_change_done, {'template_name': 'account/password_change_done.html'}, name='password_change_done'),
]
