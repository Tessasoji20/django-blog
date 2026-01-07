from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from blogs.models import Category
from blogs.models import Blog


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


def Error_404(request, exception=None):
    return render(request, '404.html', status=404)
