from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ArticleManage.models import ArticleColumn, ArticlePost

def articles_list(request, username=None):
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

	return render(request, "article/articles_list.html", {"articles":articles, "page": current_page, "username":username})

