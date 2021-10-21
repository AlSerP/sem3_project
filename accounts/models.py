from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    rating = models.IntegerField(default=0)

    class Meta(object):
        unique_together = ('email',)

    def __str__(self):
        return self.username
