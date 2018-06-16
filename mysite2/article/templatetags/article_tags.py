from django import template    #①

register = template.Library()    #②

from article.models import ArticlePost    #③

@register.simple_tag    #④
def total_articles():
    return ArticlePost.objects.count()    #⑤

@register.simple_tag
def author_total_articles(user):    #⑧
	return user.article.count()     #⑨

@register.inclusion_tag('article/list/latest_articles.html')    #①
def latest_articles(n=5):    #②
	latest_articles = ArticlePost.objects.order_by("-created")[:n]    #③
	return {"latest_articles": latest_articles}    #④
