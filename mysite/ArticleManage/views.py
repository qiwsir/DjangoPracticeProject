from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import ArticleColumn

from .forms import ArticleColumnForm

@login_required(login_url='/account/login/')
def article_column(request):
	columns = ArticleColumn.objects.all()
	return render(request, "ArticleManage/column/article_column.html", {"columns":columns})

