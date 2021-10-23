from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .forms import ImageForm
from .models import Image, Comment
from django.urls import reverse_lazy
from django.shortcuts import redirect


def does_have_permission(user, obj):
    if user != obj.user:
        raise PermissionDenied({"message": "You don't have permission to access"})


class UploadImageView(LoginRequiredMixin, CreateView):
    """Регестрация пользователя"""
    model = Image
    template_name = 'upload_image.html'
    success_url = reverse_lazy('user_images')  # используется, поскольку становится доступно с запазданием
    fields = ['title', 'image', 'tags']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.rating = 0
        return super().form_valid(form)


class ImageView(UpdateView):
    model = Image
    fields = '__all__'
    template_name = 'image/image_page.html'


class ImageUpdateView(LoginRequiredMixin, UpdateView):
    model = Image
    fields = ['title', 'tags']
    template_name = 'image/image_edit.html'

    def get(self, request, *args, **kwargs):
        does_have_permission(self.request.user, Image.objects.get(pk=self.kwargs['pk']))
        return super().get(request, *args, **kwargs)


class ImageDeleteView(LoginRequiredMixin, DeleteView):
    model = Image
    template_name = 'image/image_delete.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        does_have_permission(self.request.user, Image.objects.get(pk=self.kwargs['pk']))
        return super().get(request, *args, **kwargs)


class UploadCommentView(LoginRequiredMixin, CreateView):
    """Регестрация пользователя"""
    model = Comment
    template_name = 'comments/comment_upload.html'
    fields = ['text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.image = Image.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)


def like_image(request, **kwargs):
    image = Image.objects.get(pk=kwargs['pk'])
    image.like(request.user)
    return redirect(image.get_absolute_url())


def dislike_image(request, **kwargs):
    image = Image.objects.get(pk=kwargs['pk'])
    image.dislike(request.user)
    return redirect(image.get_absolute_url())


class AllImagesView(ListView):
    model = Image
    context_object_name = 'images'
    template_name = 'image/images.html'

    def get_queryset(self, **kwargs):
        """Request as /shaw?search=tag"""
        if self.request.GET['search']:
            return Image.objects.filter(tags__contains=self.request.GET['search'])

        return Image.objects.all()
