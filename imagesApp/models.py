from django.conf import settings
from django.db import models
from time import gmtime, strftime
from typing import List


def directory_path(instance, filename):
    upload_time = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
    return ('user_{0}/%s/{1}' % upload_time).format(instance.user.id, filename)


class Tag(models.Model):
    name = models.CharField(max_length=32, null=False, unique=True)

    class Meta(object):
        unique_together = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/images/show?search={self.name}'


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to=directory_path)
    rating = models.IntegerField(default=0)

    def get_tags(self) -> List[str]:
        return str(self.tags).split(',')

    def like(self, user) -> None:
        """Controls likes system of Image"""
        print(user.username, 'liked', self.pk)
        like_dislike = LikeDislike.objects.filter(user=user, content=self).first()
        if not like_dislike:
            like_dislike = LikeDislike(is_like=True, user=user, content=self)
            self.rating += 1
            self.save()
            like_dislike.save()
        elif not like_dislike.is_like:
            like_dislike.is_like = True
            self.rating += 2
            self.save()
            like_dislike.save()
        else:
            like_dislike.delete()
            self.rating -= 1
            self.save()

    def dislike(self, user) -> None:
        """Controls dislikes system of Image"""
        print(user.username, 'disliked', self.pk)
        like_dislike = LikeDislike.objects.filter(user=user, content=self).first()
        print(like_dislike)
        if not like_dislike:
            like_dislike = LikeDislike(is_like=False, user=user, content=self)
            self.rating -= 1
            self.save()
            like_dislike.save()
        elif like_dislike.is_like:
            like_dislike.is_like = False
            self.rating -= 2
            self.save()
            like_dislike.save()
        else:
            like_dislike.delete()
            self.rating += 1
            self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self) -> str:
        return f'/images/{self.pk}'


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return f'/images/{self.image.pk}#{self.pk}'


class LikeDislike(models.Model):
    is_like = models.BooleanField(null=False)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='likes_dislikes')
    content = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='likes_dislikes')

    def __str__(self):
        return f"{self.user} likes {self.content} is {self.is_like}"
