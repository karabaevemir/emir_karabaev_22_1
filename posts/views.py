from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from posts.models import Post, Comment, Hashtag


def main(request):
    if request.method == 'GET':
        posts = Post.objects.all()

        data = {
            'posts': posts
        }
        return render(request, 'layouts/main.html', context=data)
    
    
def posts_view(request):
    if request.method == 'GET':
        hashtag_id = request.GET.get('hashtag_id')
        if hashtag_id:
            posts = Post.objects.filter(hashtag_id=hashtag_id)
        else:
            posts = Post.objects.all()

        data = {
            'posts': posts
        }

        return render(request, 'posts/posts.html', context=data)


def post_detail_view(request, **kwargs):
    if request.method == 'GET':
        post = Post.objects.get(id=kwargs['id'])
        comments = Comment.objects.filter(post=post)

        data = {
            'post': post,
            'comments': comments
        }

        return render(request, 'posts/detail.html', context=data)


def hashtags_view(request, **kwargs):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()

        data = {
            'hashtags': hashtags
        }

        return render(request, 'hashtags/hashtags.html', context=data)


def hello(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')


def now_date(request):
    now = datetime.now()
    if request.method == 'GET':
        return HttpResponse(now.strftime("%d %B %Y (%A)"))


def bye(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user!!!')