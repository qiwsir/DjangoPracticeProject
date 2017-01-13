from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse

from slugify import slugify

from taggit.managers import TaggableManager

class ArticleColumn(models.Model):
	user = models.ForeignKey(User, related_name='article_column')
	column = models.CharField(max_length=200)
	created = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.column

class ArticleTag(models.Model):
	author = models.ForeignKey(User, related_name="tag")
	tag = TaggableManager()
	
class ArticlePost(models.Model):
	author = models.ForeignKey(User, related_name="article")
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=500)
	column = models.ForeignKey(ArticleColumn, related_name="article_column")
	body = models.TextField()
	created = models.DateTimeField(default=timezone.now())
	updated = models.DateTimeField(auto_now=True)
	users_like = models.ManyToManyField(User, related_name="articles_like", blank=True)
	article_tag = models.ManyToManyField(ArticleTag, related_name='article_tag', blank=True)

	class Meta:
		ordering = ("-updated",)
		index_together = (('id', 'slug'),)

	def __str__(self):
		return self.title

	def save(self, *args, **kargs):
		#if not self.slug:
		self.slug = slugify(self.title)
		super(ArticlePost, self).save(*args, **kargs)


	def get_absolute_url(self):
		return reverse("article:article_detail", args=[self.id, self.slug])

	def get_url_path(self):
		#return "/article/read-article/{0}/{1}".format(self.id, self.slug)
		return reverse("article_list:read_article", args=[self.id, self.slug])

