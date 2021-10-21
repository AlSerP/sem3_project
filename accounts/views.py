from .forms import CustomUserCreationForm
from .models import CustomUser
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
from django.conf import settings


class SignUpView(CreateView):
    """Регестрация пользователя"""
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'

    success_url = reverse_lazy('login')

    def form_valid(self, form):
        """Автоматический вход пользователя при удачной регистрации"""
        form.save()

        username = self.request.POST['username']
        password = self.request.POST['password1']

        user = authenticate(username=username, password=password)
        login(self.request, user)

        return super().form_valid(form)


class PasswordResetView(LoginRequiredMixin, CreateView):
    """Смена пароля пользователя"""
    form_class = CustomUserCreationForm
    template_name = 'registration/password_change_form.html'

    success_url = reverse_lazy('done')


class UserView(TemplateView):
    template_name = 'users/user_information.html'


class UpdateUserView(UpdateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'email']
    template_name = 'users/user_edit.html'

    success_url = '/user/information'

    def get_object(self):
        return self.request.user
