
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def blog_list(request):
    """blog list"""
    posts = Post.objects.all().order_by('-created_on')

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, slug):
    """blog detail page"""

    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'blog/blog_detail.html', context)
