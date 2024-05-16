from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)

    portfolio_site = models.URLField(blank=True)

    profile_photo = models.ImageField(upload_to='profile_photos', blank=True)

    def __str__(self):
        return self.user.username