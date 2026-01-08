from django.shortcuts import render,redirect

from blogs.models import Category
from blogs.models import Blog

from django.contrib.auth.decorators import login_required
from dashboards.forms import CategoryForm
from django.template.context_processors import request


@login_required(login_url='userlogin')  #only when managers,editors are loggedin,after that only they can visit dashboards
def dashboard(request):
    categories = Category.objects.all().count()
    blogs_count=Blog.objects.all().count()
    context = {
        'category_count': categories,
        'blogs_count': blogs_count,
    }
    return render(request, 'dashboard/dashboard.html', context)

def categories(request):
    return render(request, 'dashboard/categories.html')

def add_category(request):
    if request.method == 'POST':
        form_instance = CategoryForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('categories')
    form_instance = CategoryForm()
    context = {
        'form': form_instance,
    }
    return render(request, 'dashboard/add_category.html',context)

def edit_category(request, pk):

    if request.method == 'POST':
        form_instance = CategoryForm(request.POST, instance=Category.objects.get(pk=pk))
        if form_instance.is_valid():
            form_instance.save()
            return redirect('categories')
    form_instance = CategoryForm(instance=Category.objects.get(pk=pk))
    context = {
        'form': form_instance,
    }
    return render(request, 'dashboard/edit_category.html',context)

def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('categories')
