from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return self.author.username
