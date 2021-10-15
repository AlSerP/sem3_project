from django import forms
# from .models import CustomUser
from .models import Image, Comment


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('user', 'title', 'image',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('image', 'user', 'text',)
