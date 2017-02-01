from django.db import models
from django.contrib.auth.models import User

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from slugify import slugify

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('title',)

    def save(self, *args, **kargs):
        self.slug = slugify(self.title)
        super(Subject, self).save(*args, **kargs)

    def __str__(self):
        return self.title

class Course(models.Model):
    user = models.ForeignKey(User, related_name='courses_user')
    subject = models.ForeignKey(Subject, related_name='courses')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kargs)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lesson')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class BaseItem(models.Model):
    user = models.ForeignKey(User, related_name='%(class)s_related')
    title = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("-created",)

    def __str__(self):
        return self.title

class Text(BaseItem):
    content = models.TextField()

class File(BaseItem):
    file = models.FileField(upload_to='files')

class Image(BaseItem):
    image = models.ImageField(upload_to="images")

class Video(BaseItem):
    url = models.URLField()

class Content(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='contents')
    content_type = models.ForeignKey(ContentType, limit_choices_to={'model__in':('text', 'file', 'image', 'video')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
