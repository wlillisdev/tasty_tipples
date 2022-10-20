
# from .models import Post
# from django.shortcuts import render, redirect
# from django.views.generic import ListView

# # Create your views here.


# class PostListView(ListView):
#     """Class to show the posts in list view on home page """
#     model = Post
#     template_name = 'blog/blog_list.html'
#     context_object_name = 'posts'
#     ordering = ['-date_posted']
#     paginate_by = 6


# def blog_detail(request, slug):
#     """View to access blog detail page"""

#     post = get_object_or_404(Post, slug=slug)
#     context = {
#         'post': post,
#     }
#     return render(request, 'blog/blog_detail.html', context)

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
