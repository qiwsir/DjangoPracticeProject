from django.urls import path 
from . import views 

app_name = 'image'

urlpatterns = [
    path('list-images/', views.list_images, name="list_images"),
    path('upload-image/', views.upload_image, name='upload_image'), 
    path('del-image/', views.del_image, name='del_image'),
    path('images/', views.falls_images, name="falls_images"),
    ]
