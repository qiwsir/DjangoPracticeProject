from django.db import models
from django.contrib.auth.models import User

from slugify import slugify    #①
from sorl.thumbnail import ImageField

class Image(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="images")    #②
	title = models.CharField(max_length=300)    #③
	url = models.URLField()    #④
	slug = models.SlugField(max_length=500, blank=True)    #⑤
	description = models.TextField(blank=True)    #⑥
	created = models.DateField(auto_now_add=True, db_index=True)    #⑦
	image = models.ImageField(upload_to='images/%Y/%m/%d')    #⑧

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):    #⑨
		self.slug = slugify(self.title)
		super(Image, self).save(*args, **kwargs)