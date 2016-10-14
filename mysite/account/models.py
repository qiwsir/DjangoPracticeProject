from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    joined = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20)

    class Meta:
        ordering = ("-joined",)

