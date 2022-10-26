
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from django.views.generic import ListView


class BlogView(ListView):
    paginate_by = 3
    model = Post
    template_name = 'blog/blog_list.html'
    ordering = ['-created_on']


# def blog_list(request):
#     """blog list"""
#     posts = Post.objects.all().order_by('-created_on')

#     context = {
#         'posts': posts,
#     }

#     return render(request, 'blog/blog_list.html', context)


def blog_detail(request, slug):
    """blog detail page"""

    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'blog/blog_detail.html', context)
