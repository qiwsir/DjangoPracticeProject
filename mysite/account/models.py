from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):    #①
    user = models.OneToOneField(User, unique=True)   #②
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return 'user {}'.format(self.user.username)

class UserInfo(models.Model):
    user = models.OneToOneField(User, unique=True)
    school = models.CharField(max_length=97, blank=True)
    company = models.CharField(max_length=97, blank=True)
    profession = models.CharField(max_length=27, blank=True)
    address = models.CharField(max_length=177, blank=True)
    aboutme = models.TextField(blank=True)  
    photo = models.ImageField(blank=True)

    def __str__(self):
        return "user:{}".format(self.user.username)

