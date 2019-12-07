from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView
from .forms import CommentForm

from .models import Category, Post, Tag, Comment

from models import*

class PostListView(View):
    """вывод категорий"""

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=datetime.now(), published=True)

    def get(self, request, category_slug=None,slug=None):

        category_list = Category.objects.filter(published=True)

        if category_slug is not None:

            posts = self.get_queryset().filter(category__slug = category_slug,category__published = True, published = True )

        elif slug is not None:

            posts = self.get_queryset().filter(tags__slug=slug, tags__published=True)

        else:
            posts = self.get_queryset()

        if posts.exists():
            template = posts.first().get_category_template()
        else:
            template = 'blog/post_list.html'
        return render(request, template,{'post_list':posts,'categories': category_list})



class PostDetailView(View):
    """Вывод полной статьи"""
    def get(self,request, **kwargs):

        category_list = Category.objects.filter(published=True)
        post = get_object_or_404(Post,slug= kwargs.get("slug"))

        form = CommentForm()

        return render(request, post.template, {'post': post, 'categories':category_list,'form':form})

    def post(self,request,**kwargs):
        print(request.POST)
        print('**kwargs', kwargs)

        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = Post.objects.get(slug=kwargs.get("slug"))
            print(': form.post_id: ',form.post_id)
            form.author = request.user
            form.save()
        return redirect(request.path)

