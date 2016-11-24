from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)

class UserInfo(models.Model):
    user = models.OneToOneField(User, unique=True)
    school = models.CharField(max_length=97)
    company = models.CharField(max_length=97)
    profession = models.CharField(max_length=27)
    address = models.CharField(max_length=177)
    aboutme = models.TextField()

    def __str__(self):
        return "user:{}".format(self.user.username)


