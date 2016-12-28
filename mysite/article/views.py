from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ArticleManage.models import ArticleColumn, ArticlePost

def list_articles(request, username=None):
	if username:
		user = User.objects.get(username=username)
		articles_title = ArticlePost.objects.fileter(author=user)
	else:
		articles_title = ArticlePost.objects.all()

	paginator = Paginator(articles_title, 2)    
	page = request.GET.get('page')
	try:
		current_page = paginator.page(page)
		articles = current_page.object_list
	except PageNotAnInteger:
		current_page = paginator.page(1)
		articles = current_page.object_list
	except EmptyPage:
		current_page = paginator.page(paginator.num_pages)
		articles = current_page.object_list

	return render(request, "article/list_articles.html", {"articles":articles, "page": current_page})

def read_article(request, id, slug):
	article = get_object_or_404(ArticlePost, id=id, slug=slug)
	return render(request, "article/read_article.html", {"article":article})