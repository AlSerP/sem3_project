from django.db import models
from django.contrib.auth.models import AbstractUser


def directory_path(instance, filename):
    return f'user_{instance.id}/avatar/{filename}'


class CustomUser(AbstractUser):
    rating = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to=directory_path, null=True, default=None)

    class Meta(object):
        unique_together = ('email',)

    def __str__(self):
        return self.username
