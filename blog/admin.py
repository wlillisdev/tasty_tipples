'''
    imports admin.py
'''
from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


# Register Post models.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    '''
        Class to control what will be shown on posts
    '''
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
