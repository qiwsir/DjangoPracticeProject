from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    joined = models.DateTimeField(default=timezone.now)
    phone = models.CharField(max_length=20, null=True)

    class Meta:
        ordering = ("-joined",)

