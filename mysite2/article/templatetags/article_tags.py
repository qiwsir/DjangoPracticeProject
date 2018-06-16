from django import template    #①

register = template.Library()    #②

from article.models import ArticlePost    #③
from django.db.models import Count

from django.utils.safestring import mark_safe
import markdown


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


@register.simple_tag    #①
def most_commented_articles(n=3):    #②
	return ArticlePost.objects.annotate(total_comments=Count('comments')).order_by("-total_comments")[:n]    #③


@register.filter(name='markdown')    #①
def markdown_filter(text):    #②
	return mark_safe(markdown.markdown(text))    #③
