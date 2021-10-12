from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView
from .forms import ImageForm
from .models import Image
from django.urls import reverse_lazy
from django.shortcuts import redirect


class UploadImageView(CreateView):
    """Регестрация пользователя"""
    model = Image
    template_name = 'upload_image.html'
    success_url = reverse_lazy('home')  # используется, поскольку становится доступно с запазданием
    fields = ['title', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.rating = 0
        return super().form_valid(form)


class ImageView(UpdateView):
    model = Image
    fields = '__all__'
    template_name = 'image/image_page.html'


class ImageUpdateView(UpdateView):
    model = Image
    fields = ['title']
    template_name = 'image/image_edit.html'


class ImageDeleteView(DeleteView):
    model = Image
    template_name = 'image/image_delete.html'
    success_url = reverse_lazy('home')
