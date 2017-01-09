from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from ArticleManage.models import ArticlePost

class Comment(models.Model):
	article = models.ForeignKey(ArticlePost, related_name="comments")
	commentator = models.ForeignKey(User, related_name="commentator")
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return "Comment by {0} on {1}".format(self.commentator.username, self.article)