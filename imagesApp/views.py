from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import PermissionDenied
from .forms import ImageForm, ImageUpdate
from .models import Image, Comment, Tag
from django.urls import reverse_lazy
from django.shortcuts import redirect


def does_have_permission(user, obj):
    if user != obj.user:
        raise PermissionDenied({"message": "You don't have permission to access"})


class ImageView(UpdateView):
    model = Image
    fields = '__all__'
    template_name = 'images/image_page.html'


class UploadImageView(LoginRequiredMixin, CreateView):
    """Регестрация пользователя"""
    model = Image
    form_class = ImageForm
    template_name = 'upload_image.html'
    success_url = reverse_lazy('user_images')  # используется, поскольку становится доступно с запазданием

    def form_valid(self, form):
        image = form.save(commit=False)
        user = self.request.user
        form.instance.user = user
        form.instance.rating = 0
        form.save()
        for tag in form.cleaned_data['tags'].replace(' ', '').split(','):  # TODO: Вынести в функцию
            tag_obj: Tag
            if Tag.objects.filter(name=tag).exists():
                tag_obj = Tag.objects.get(name=tag)
            else:
                tag_obj: Tag = Tag(name=tag)
                tag_obj.save()
            form.instance.tags.add(tag_obj)
            form.save()
        return super(UploadImageView, self).form_valid(form)


class ImageUpdateView(LoginRequiredMixin, UpdateView):
    model = Image
    form_class = ImageUpdate
    template_name = 'images/image_edit.html'

    def get(self, request, *args, **kwargs):
        does_have_permission(self.request.user, Image.objects.get(pk=self.kwargs['pk']))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        image = form.save(commit=False)
        form.save()
        for tag in form.cleaned_data['tags'].replace(' ', '').lower().split(','):  # TODO: Вынести в функцию
            if tag.replace(' ', ''):
                tag_obj: Tag
                if Tag.objects.filter(name=tag).exists():
                    tag_obj = Tag.objects.get(name=tag)
                else:
                    tag_obj: Tag = Tag(name=tag)
                    tag_obj.save()
                form.instance.tags.add(tag_obj)
                form.save()
        return super(ImageUpdateView, self).form_valid(form)


class ImageDeleteView(LoginRequiredMixin, DeleteView):
    model = Image
    template_name = 'images/image_delete.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        does_have_permission(self.request.user, Image.objects.get(pk=self.kwargs['pk']))
        return super().get(request, *args, **kwargs)


class AllImagesView(ListView):
    model = Image
    context_object_name = 'images'
    template_name = 'images/images.html'

    def get_queryset(self, **kwargs):
        """Request as /shaw?search=tag"""
        try:
            tag_name = self.request.GET['search']
            if Tag.objects.filter(name=tag_name).exists():
                # return Image.objects.filter(tags__contains=self.request.GET['search'])
                return Tag.objects.get(name=tag_name).image_set.all()
        except MultiValueDictKeyError:
            return Image.objects.all()


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


def delete_tag(request, **kwargs):
    image = Image.objects.get(pk=kwargs['pk'])
    tag = Tag.objects.get(name=kwargs['tag'])
    image.tags.remove(tag)
    return redirect(image.get_absolute_url() + '/edit')
