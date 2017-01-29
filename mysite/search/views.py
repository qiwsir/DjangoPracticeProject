from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from ArticleManage.models import ArticlePost

from functools import reduce

@csrf_exempt
def search_articles(request):
    if request.method == "POST":
        searching_words = request.POST['word'].split()
        results = ArticlePost.objects.filter(reduce(lambda x, y: x | y, [Q(body__contains=word) for word in searching_words]))
        print(results)
        serialized_result = serializers.serialize('json', results)
        #return JsonResponse({'results':serialized_result})
        return HttpResponse(serialized_result)
    return render(request, 'search/search_articles.html', {})
