from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category,Blog




def home(request):

    featured_posts = Blog.objects.filter(is_featured=True,status='published')
    posts = Blog.objects.filter(is_featured=False,status='published')


    context = {  #categories passed thru context-processors
               'featured_posts':featured_posts,
               'posts':posts
               }
    return render(request, 'home.html',context)