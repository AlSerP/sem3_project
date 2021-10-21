# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from imagesApp.models import Image


class HomePageView(ListView):
    model = Image
    context_object_name = 'images'  # Name of list
    template_name = 'home.html'

    def get_queryset(self):
        # if self.request.user.is_authenticated:
        #     user = CustomUser.objects.get(id=self.request.user.id)  # filter by user
        #     return Image.objects.filter(user=user)
        return Image.objects.all()[:5]


class TestPageView(ListView):
    model = Image
    context_object_name = 'images'
    template_name = 'index.html'

    def get_queryset(self):
        return Image.objects.all()[:3]


class UserImagesView(LoginRequiredMixin, ListView):
    model = Image
    context_object_name = 'images'  # Name of list
    template_name = 'user_images.html'

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)
