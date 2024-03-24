from django.shortcuts import render
from .models import Post


def posts_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/posts_list.html', {'posts': posts})


def single_post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/single_post_page.html', {'post': post})


def new_post_page(request):
    return render(request, 'blog/new_post_page.html')
