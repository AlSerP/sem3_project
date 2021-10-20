from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('user/', include('accounts.urls')),
    path('user/', include('django.contrib.auth.urls')),
    path('images/', include('imagesApp.urls')),
    path('', include('pages.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
