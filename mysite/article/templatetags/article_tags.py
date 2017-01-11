from django import template

register = template.Library()

from ArticleManage.models import ArticlePost

@register.simple_tag
def total_articles():
    return ArticlePost.objects.count()

@register.simple_tag()
def author_total_articles(user):    
	return user.article.count()
	