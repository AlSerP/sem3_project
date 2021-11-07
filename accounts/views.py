from .forms import CustomUserCreationForm, CustomUserChangeFrom
from .models import CustomUser
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
from django.conf import settings
from django.contrib.auth import authenticate
from django.shortcuts import redirect


class SignUpView(CreateView):
    """Регестрация пользователя"""
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'

    success_url = reverse_lazy('login')

    def form_valid(self, form):
        """Автоматический вход пользователя при удачной регистрации"""
        form.save()

        username = self.request.POST['id_username']
        password = self.request.POST['id_password1']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)

        return super().form_valid(form)


class PasswordResetView(LoginRequiredMixin, CreateView):
    """Смена пароля пользователя"""
    form_class = CustomUserCreationForm
    template_name = 'registration/password_change_form.html'

    success_url = reverse_lazy('done')


class UserView(TemplateView):
    """Отображение информации пользователя"""
    template_name = 'users/user_information.html'


class UpdateUserView(UpdateView):
    """Обновление настроек пользователя"""
    model = CustomUser
    form_class = CustomUserChangeFrom
    template_name = 'users/user_edit.html'

    success_url = '/user/information'

    def get_object(self):
        return self.request.user


def login_user(request):
    username = request.POST['id_username']
    password = request.POST['id_password']
    user = authenticate(username='john', password='secret')
    if user is not None:
        login(request, user)
        redirect('/')
    else:
        redirect('/')
