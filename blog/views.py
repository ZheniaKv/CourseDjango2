from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Category, Post

from models import*


class HomeView(View):
    """вывод всех постов"""
    def get(self,request):
        category_list = Category.objects.all()
        post_list = Post.objects.all()
        return render(request,'blog/home.html', {'categories': category_list, 'posts': post_list})


class CategoryView(View):
    """Вывод статей категории"""
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        return render(request, 'blog/home.html', {'category': category})


