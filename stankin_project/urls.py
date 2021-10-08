from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/', include('accounts.urls'), name='login'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('', include('pages.urls')),
]
