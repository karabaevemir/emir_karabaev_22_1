from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from posts.forms import PostCreateForm, CommentCreateForm
from posts.models import Post, Comment, Hashtag
from users.utils import get_user_from_request
from django.views.generic import ListView, CreateView

PAGINATION_LIMIT = 4


class HashtagsView(ListView):
    model = Hashtag
    template_name = 'hashtags/hashtags.html'

    def get(self, request,*args, **kwargs):
        context = {
            'object_list': self.get_queryset(),
            'user': get_user_from_request(request)
        }
        return render(request, self.template_name, context=context)
    
    
class PostsCreateView(ListView, CreateView):
    model = Post
    template_name = 'posts/create.html'
    form_class = PostCreateForm

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'form': kwargs['form'] if kwargs.get('form') else self.form_class,
            'user': get_user_from_request(self.request)
        }

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            self.model.objects.create(
                author_id=1,
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate'),
                hashtag_id=form.cleaned_data.get('hashtag')
            )
            return redirect('/posts')
        else:
            return render(request, self.template_name, context=self.get_context_data(form=form))


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
        search_text = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if hashtag_id:
            posts = Post.objects.filter(hashtag_id=hashtag_id)
        else:
            posts = Post.objects.all()

        if search_text:
            posts = posts.filter(title__icontains=search_text)

        max_page = round(posts.__len__() / PAGINATION_LIMIT)

        posts = posts[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        data = {
            'posts': posts,
            'user': get_user_from_request(request),
            'hashtag_id': hashtag_id,
            'current_page': page,
            'max_page': range(1, max_page+1)
        }

        return render(request, 'posts/posts.html', context=data)


def post_detail_view(request, **kwargs):
    if request.method == 'GET':
        post = Post.objects.get(id=kwargs['id'])
        comments = Comment.objects.filter(post=post)

        data = {
            'post': post,
            'comments': comments,
            'form': CommentCreateForm,
            'user': get_user_from_request(request)
        }

        return render(request, 'posts/detail.html', context=data)
    if request.method == 'POST':
        form = CommentCreateForm(data=request.POST)

        if form.is_valid():
            Comment.objects.create(
                author_id=2,
                text=form.cleaned_data.get('text'),
                post_id=kwargs['id']
            )
            return redirect(f'/posts/{kwargs["id"]}/')
        else:
            post = Post.objects.get(id=kwargs['id'])
            comments = Comment.objects.filter(post=post)

            data = {
                'post': post,
                'comments': comments,
                'form': form
            }
            return render(request, 'posts/detail.html', context=data)


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


