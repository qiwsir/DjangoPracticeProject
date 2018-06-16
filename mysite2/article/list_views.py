from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.models import User
from .models import ArticleColumn, ArticlePost 

# def article_titles(request, username=None):
# 	if username:
# 		user = User.objects.get(username=username)
# 		articles_title = ArticlePost.objects.filter(author=user)
# 	else:
# 		articles_title = ArticlePost.objects.all()
	
# 	#articles_title = ArticlePost.objects.all()
# 	paginator = Paginator(articles_title, 2)    
# 	page = request.GET.get('page')
# 	try:
# 		current_page = paginator.page(page)
# 		articles = current_page.object_list
# 	except PageNotAnInteger:
# 		current_page = paginator.page(1)
# 		articles = current_page.object_list
# 	except EmptyPage:
# 		current_page = paginator.page(paginator.num_pages)
# 		articles = current_page.object_list

# 	return render(request, "article/list/article_titles.html", {"articles":articles, "page": current_page})


def article_titles(request, username=None):
	if username:
		user = User.objects.get(username=username)
		articles_title = ArticlePost.objects.filter(author=user)
		try:
		    userinfo = user.userinfo    #④
		except:
			userinfo = None
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

	if username:
		return render(request, "article/list/author_articles.html", {"articles":articles, "page":current_page, "userinfo":userinfo, "user":user})    #⑤
	return render(request, "article/list/article_titles.html", {"articles":articles, "page": current_page})


def article_detail(request, id, slug):
	print(id, slug)
	article = get_object_or_404(ArticlePost, id=id, slug=slug)
	return render(request, "article/list/article_detail.html", {"article":article})
