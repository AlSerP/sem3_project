from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.SignUpView.as_view(), name="signup"),
    path('settings', views.UpdateUserView.as_view(), name="user_settings"),
    path('information', views.UserView.as_view(), name="user_info"),
    path('login', views.login_user, name='login'),
    # path('password_change', views.PasswordResetView.as_view(), name="password_reset"),
    # path('successful', views.PasswordResetView.as_view(), name="done"),
]
