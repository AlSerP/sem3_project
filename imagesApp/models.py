from django.conf import settings
from django.db import models
from time import gmtime, strftime


def directory_path(instance, filename):
    upload_time = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
    return ('user_{0}/%s/{1}' % upload_time).format(instance.user.id, filename)


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to=directory_path)
    rating = models.IntegerField(default=0)

    def like(self, user):
        # print(user.username, 'get liked', self.pk)
        self.rating += 1
        self.save()

    def dislike(self, user):
        print(user.username, 'get liked', self.pk)
        self.rating -= 1
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/images/{self.pk}'
    # TODO: get_absolute_url


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return f'/images/{self.image.pk}#{self.pk}'
