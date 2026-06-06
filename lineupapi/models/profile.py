
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.CharField(max_length=3500)
    soundcloud = models.URLField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255, blank=True)