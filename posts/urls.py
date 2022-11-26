from django.urls import path

from posts.views import posts_view, post_detail_view, hashtags_view

urlpatterns = [
    path('posts/', posts_view),
    path('posts/<int:id>/', post_detail_view),
    path('hashtags/', hashtags_view),
]