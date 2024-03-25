from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import CreatePost


def posts_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/posts_list.html', {'posts': posts})


def single_post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/single_post_page.html', {'post': post})


@login_required(login_url="auth:login")
def new_post_page(request):
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author_id = request.user
            new_post.save()
            return redirect('blog:list')
    else:
        form = CreatePost()
    return render(request, 'blog/new_post_page.html', {'form': form})
