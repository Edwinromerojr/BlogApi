from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('get_all_posts/', views.getAllPosts),
    path('create_post/', views.createPost),
    path('delete_post/', views.deletePost),
    path('get_post/', views.getPost),
    path('update_post/', views.updatePost),
    
]