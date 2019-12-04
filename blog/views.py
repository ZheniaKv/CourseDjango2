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
        posts = Post.objects.filter(published_date__lte=datetime.now(), published=True)
        return render(request,'blog/post_list.html', {'categories': category_list, 'post_list': posts})


class CategoryView(View):
    """вывод категорий"""
    def get(self, request, slug):
        posts = Post.objects.filter(category__slug = slug,category__published = True, published = True )
        return render(request, 'blog/post_list.html',{'post_list':posts})



class TagView(View):
    """вывод статей по тегу"""
    def get(self, request, slug):
        current_tag = Tag.objects.get(slug=slug)
        pk = current_tag.id
        posts = Post.objects.filter(tags__id=pk)

        return render(request, 'blog/post_list.html', {'post_list': posts})


class PostDetailView(View):
    """Вывод полной статьи"""
    def get(self,request, category, slug):
        category_list = Category.objects.all()
        post = Post.objects.get(slug=slug)
        return render(request, post.template, {'post': post, 'categories':category_list})
