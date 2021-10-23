from django import forms
# from .models import CustomUser
from .models import Image, Comment


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image')

    tags = forms.CharField()


class ImageUpdate(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title',)

    tags = forms.CharField(required=False)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('image', 'user', 'text',)
