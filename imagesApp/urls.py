from django.urls import path

from . import views

urlpatterns = [
    path('upload', views.UploadImageView.as_view(), name="upload"),
    path('all', views.AllImagesView.as_view(), name="all_images"),
    path('<int:pk>/', views.ImageView.as_view(), name='image_show'),
    path('<int:pk>/edit/', views.ImageUpdateView.as_view(), name='image_edit'),
    path('<int:pk>/delete/', views.ImageDeleteView.as_view(), name='image_delete'),
    path('<int:pk>/comment/', views.UploadCommentView.as_view(), name='comment_upload'),
    path('<int:pk>/like/', views.like_image, name='like'),
    path('<int:pk>/dislike/', views.dislike_image, name='dislike'),
]
