from django.db import models
from django.contrib.auth.models import User

from slugify import slugify 

class Image(models.Model):
    user = models.ForeignKey(User, related_name="images") 
    title = models.CharField(max_length=300)   
    url = models.URLField()   
    slug = models.SlugField(max_length=500, blank=True) 
    description = models.TextField(blank=True)   
    created = models.DateField(auto_now_add=True, db_index=True)  
    image = models.ImageField(upload_to='images/%Y/%m/%d')   

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  
        self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)

