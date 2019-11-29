
from . import views
from django.urls import path

urlpatterns = [

 path('category/<slug:slug>/', views.CategoryView.as_view(), name='category'),
 path('', views.HomeView.as_view()),
 path("<slug:category>/<slug:slug>/", views.PostDetailView.as_view(), name="detail_post"),
 path('tag<slug:slug>/',views.TagView.as_view(),name = 'find_by_tag' ),

]