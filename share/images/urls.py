from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('detail/<int:id>/<slug:slug>/', views.image_detail, name='detail'),
    path('like/', views.image_like, name='like'),
    path('', views.image_list, name='list'),

    path('user_images_list/<int:user_id>/', views.user_images_list, name='user_images_list'),
    path('delete/<int:id_image>', views.delete, name='delete'),
    path('download/<int:id_image>/', views.download_image, name='download_image'),
]