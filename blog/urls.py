from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogView.as_view(), name='blogview'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
]
