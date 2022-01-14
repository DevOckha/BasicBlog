from django.http import HttpResponse, request
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    posts = Post.objects.filter(active=True, featured=True)[0:2]
    context = {'posts':posts}
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def posts(request):
    posts = Post.objects.filter(active=True)

    page = request.GET.get('page')

    paginator = Paginator(posts, 5)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    context = {'posts':posts}
    return render(request, 'posts.html', context)


def post(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post':post}
    return render(request, 'post.html', context)

