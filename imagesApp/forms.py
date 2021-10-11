from django import forms
# from .models import CustomUser
from .models import Image


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('user', 'title', 'image',)
