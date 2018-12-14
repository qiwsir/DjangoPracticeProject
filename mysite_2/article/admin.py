from django.contrib import admin
from .models import ArticleColumn

class ArticleColumnAdmin(admin.ModelAdmin): 
    list_display = ('column', 'created', 'user') 
    list_filter = ("column",)
    
admin.site.register(ArticleColumn, ArticleColumnAdmin)

# Register your models here.
