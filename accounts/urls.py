from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.SignUpView.as_view(), name="signup"),
    # path('password_change', views.PasswordResetView.as_view(), name="password_reset"),
    # path('successful', views.PasswordResetView.as_view(), name="done"),
]
