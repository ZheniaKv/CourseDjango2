from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import DetailView

from .models import Category, Post, Tag

from models import*


class HomeView(View):

    """вывод всех постов"""
    def get(self,request):
        category_list = Category.objects.all()
        post_list = Post.objects.filter(published_date__lte=datetime.now(), published=True)
        return render(request,'blog/single_post.html', {'categories': category_list, 'post_list': post_list})


class CategoryView(View):

    """Вывод категорий"""
    def get(self, request,category, slug):
        category = Category.objects.get(slug=slug)
        return render(request, 'blog/home.html', {'category': category})


class PostDetailView(View):
    """Вывод полной статьи"""
    def get(self,request, category, slug):
        category_list = Category.objects.all()
        post = Post.objects.get(slug=slug)

        return render(request, 'blog/post_detail.html', {'post': post, 'categories':category_list})


