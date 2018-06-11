from django.shortcuts import render
from .models import BlogArticles

def blog_title(request):    #②
    blogs = BlogArticles.objects.all()    #③
    return render(request, "blog/titles.html", {"blogs":blogs})    #④
