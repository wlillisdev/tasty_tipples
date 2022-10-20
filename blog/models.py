from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post Model
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    # Sort the blog creation date from the recent date first
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
