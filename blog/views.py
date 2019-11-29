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
        return render(request,'blog/post_list.html', {'categories': category_list, 'post_list': post_list})


class CategoryView(View):
    """вывод категорий"""
    def get(self, request, slug):
        current_category = Category.objects.get(slug=slug)
        pk = current_category.id
        posts = Post.objects.filter(category = pk)
        return render(request, 'blog/category_list.html',{'category_posts':posts,'name': current_category})



class TagView(View):
    """вывод статей по тегу"""
    def get(self, request, slug):

        current_tag = Tag.objects.get(slug=slug)
        pk = current_tag.id
        posts_by_tag = Post.objects.filter(tags__id=pk)

        return render(request, 'blog/post_list.html', {'posts_by_tag': posts_by_tag})



class PostDetailView(View):
    """Вывод полной статьи"""
    def get(self,request, category, slug):
        category_list = Category.objects.all()
        post = Post.objects.get(slug=slug)
        return render(request, post.template, {'post': post, 'categories':category_list})





