from django.db import models
from django.conf import settings

# Create your models here.

class Favourites(models.Model):
    pass

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    favourites = models.ForeignKey(Favourites, on_delete=models.CASCADE, related_name="profile", null=True, blank=True)
    location = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, blank=True, null=True)
