from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from posts.models import Post


def main(request):
    if request.method == 'GET':
        posts = Post.objects.all()

        data = {
            'posts': posts
        }
        return render(request, 'layouts/main.html', context=data)
    
    
def posts_view(request):
    if request.method == 'GET':
        category_id = request.GET.get('category_id')
        if category_id:
            posts = Post.objects.filter(category_id=category_id)
        else:
            posts = Post.objects.all()

        data = {
            'posts': posts
        }

        return render(request, 'posts/posts.html', context=data)
    

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