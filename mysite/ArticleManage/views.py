from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import ArticleColumn, ArticlePost
from django.contrib.auth.models import User

from .forms import ArticleColumnForm, ArticlePostForm

@login_required(login_url='/account/login/')
@csrf_exempt
def article_column(request):
	if request.method == "GET":
	    columns = ArticleColumn.objects.all()
	    column_form = ArticleColumnForm()
	    return render(request, "ArticleManage/column/article_column.html", {"columns":columns, 'column_form':column_form})

	if request.method == "POST":
		column_name = request.POST['column']
		has_column = ArticleColumn.objects.filter(column=column_name)
		if has_column:
			return HttpResponse('2')
		else:
		    user = User.objects.get(username=request.user.username)
		    ArticleColumn.objects.create(user=user, column=column_name)
		    return HttpResponse("1")

@login_required(login_url='/account/login')
@require_POST
@csrf_exempt
def rename_article_column(request):
	column_name = request.POST["column_name"]
	column_id = request.POST['column_id']
	try:
	    line = ArticleColumn.objects.get(id=column_id)
	    line.column = column_name
	    line.save()
	    return HttpResponse("1")
	except:
		return HttpResponse("0")

@login_required(login_url='/account/login')
@require_POST
@csrf_exempt
def del_article_column(request):
	column_id = request.POST["column_id"]
	try:
	    line = ArticleColumn.objects.get(id=column_id)
	    line.delete()
	    return HttpResponse("1")
	except:
		return HttpResponse("2")

@login_required(login_url='/account/login')
def article_list(request, column=None):
	if column:
		articles = ArticlePost.objects.filter(column=column)
	else:
		articles = ArticlePost.objects.all()
	return render(request, "ArticleManage/article/article_list.html", {"articles":articles})

@login_required(login_url='/account/login')
def article_detail(request, id, slug):
	article = get_object_or_404(ArticlePost, id=id, slug=slug)
	return render(request, "ArticleManage/article/article_detail.html", {"article":article})

@login_required(login_url='/account/login')
@csrf_exempt
def article_post(request):
	if request.method=="POST":
		article_post_form = ArticlePostForm(data=request.POST)
		if article_post_form.is_valid():
			cd = article_post_form.cleaned_data
			try:
 			    new_article = article_post_form.save(commit=False)
 			    new_article.author = request.user
 			    new_article.column = request.user.article_column.get(id=request.POST['column_id'])
 			    new_article.save()
 			    return HttpResponse("1")
			except:
				return HttpResponse("2")
	else:
		article_post_form = ArticlePostForm()
		article_columns = request.user.article_column.all()
		#article_columns = ArticleColumn.objects.filter(user=request.user)
		return render(request, "ArticleManage/article/article_post.html", {"article_post_form":article_post_form, "article_columns":article_columns})


