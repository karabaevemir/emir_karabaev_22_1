from django.urls import path

from posts.views import posts_view, post_detail_view, post_create_view, HashtagsView, PostsCreateView

urlpatterns = [
    path('posts/', posts_view),
    path('posts/<int:id>/', post_detail_view),
    path('hashtags/', HashtagsView.as_view()),
    path('posts/create/', PostsCreateView.as_view())
]