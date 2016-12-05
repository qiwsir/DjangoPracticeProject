from django.db import models
from django.contrib.auth.models import User

class ArticleColumn(models.Model):
	user = models.ForeignKey(User, related_name='article_column')
	column = models.CharField(max_length=200)
	created = models.DateField(auto_now_add=True, db_index=True)

	def __str__(self):
		return self.column
	
