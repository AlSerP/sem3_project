from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    # path('', views.TestPageView.as_view(), name="home"),
    path('my_images', views.UserImagesView.as_view(), name="user_images"),
    path('category', views.CategoryPageView.as_view(), name="category"),
    path('test', views.TestPageView.as_view(), name="test"),
]
