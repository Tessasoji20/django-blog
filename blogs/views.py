from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from blogs.models import Category
from blogs.models import Blog
from django.db.models import Q

# Create your views here.
def posts_by_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts=Blog.objects.filter(status='published',category=category)
    # try:
    #     category=Category.objects.get(pk=pk)
    # except:
    #     #if category does not exists redirect to home
    #     return redirect('error404')

    #OR use the below code when to show 404 error page
    # category=get_object_or_404(Category,pk=pk)

    context={
        'posts':posts,
        'category':category,
    }
    return render(request,'posts_by_category.html',context)

def blogs(request,slug):
    single_blog=get_object_or_404(Blog,slug=slug,status='published')
    context={
        'single_blog':single_blog,
    }
    return render(request,'blogs.html',context)

def Error_404(request, exception=None):
    return render(request, '404.html', status=404)

def search(request):
    keyword=request.GET.get('keyword')
    blogs=Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword))

    context={
        'blogs':blogs,
        'keyword':keyword,
    }
    return render(request, 'search.html', context)
