from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(CreateView):
    """Регестрация пользователя"""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')  # используется, поскольку становится доступно с запазданием
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        """Автоматический вход пользователя при удачной регистрации"""
        form.save()

        username = self.request.POST['username']
        password = self.request.POST['password1']

        user = authenticate(username=username, password=password)
        login(self.request, user)


class PasswordResetView(LoginRequiredMixin, CreateView):
    """Смена пароля пользователя"""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('done')
    template_name = 'registration/password_change_form.html'
