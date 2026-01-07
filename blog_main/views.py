from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category,Blog

from blogs.models import About


def home(request):

    featured_posts = Blog.objects.filter(is_featured=True,status='published')
    posts = Blog.objects.filter(is_featured=False,status='published')
    #try will work only when get(){single entrt is there}
    try:
        about=About.objects.get()
    except:
        about=None

    context = {  #categories passed thru context-processors
               'featured_posts':featured_posts,
               'posts':posts,
                'about':about,

               }
    return render(request, 'home.html',context)