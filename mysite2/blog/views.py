from django.shortcuts import render
from .models import BlogArticles

def blog_title(request):    #②
    blogs = BlogArticles.objects.all()    #③
    return render(request, "blog/titles.html", {"blogs":blogs})    #④

def blog_article(request, article_id):    #①
    article = BlogArticles.objects.get(id=article_id)    #②
    pub = article.publish
    return render(request, "blog/content.html", {"article":article, "publish":pub })
