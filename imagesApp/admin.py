from django.contrib import admin
from .models import Image, Comment, Tag


admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Tag)
