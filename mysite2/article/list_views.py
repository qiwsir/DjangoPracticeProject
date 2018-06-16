from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse

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

@csrf_exempt
@require_POST
@login_required(login_url='/account/login/')
def like_article(request):
	article_id = request.POST.get("id")    #①
	action = request.POST.get("action")    #②
	if article_id and action:
		try:
			article = ArticlePost.objects.get(id=article_id)
			if action=="like":
				article.users_like.add(request.user)    #③
				return HttpResponse("1")
			else:
				article.users_like.remove(request.user)    #④
				return HttpResponse("2")
		except:
			return HttpResponse("no")
