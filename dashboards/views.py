from django.shortcuts import render,redirect

from blogs.models import Category
from blogs.models import Blog
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,user_passes_test
from dashboards.forms import CategoryForm
from django.template.context_processors import request

from dashboards.forms import BlogForm
from django.template.defaultfilters import slugify

from dashboards.forms import AddUserForm,EditUserForm



def is_manager_or_editor(user):
    return user.groups.filter(name__in=['Manager', 'Editor']).exists()


@login_required(login_url='userlogin')

#only when managers,editors are loggedin,after that only they can visit dashboards
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

def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'dashboard/posts.html',context)

def add_post(request):
    if request.method == 'POST':
        form_instance = BlogForm(request.POST,request.FILES)
        if form_instance.is_valid():
            p=form_instance.save(commit=False)
            p.author = request.user
            p.save()   #only then we will get id for p.slug uniqueness
            data = form_instance.cleaned_data
            title = data['title']
            p.slug = slugify(title) + '-'+str(p.id) #to make it unique(PK)
            p.save()
            return redirect('posts')
    form_instance=BlogForm()
    context = {
        'form': form_instance,
    }
    return render(request, 'dashboard/add_post.html',context)

def edit_post(request, pk):
    if request.method == 'POST':
        form_instance = BlogForm(request.POST,request.FILES, instance=Blog.objects.get(pk=pk))
        if form_instance.is_valid():
            p=form_instance.save()
            data = form_instance.cleaned_data
            title = data['title']
            p.slug = slugify(title) + '-'+str(p.id)
            p.save()
            return redirect('posts')
    form_instance = BlogForm(instance=Blog.objects.get(pk=pk))
    context = {
        'form': form_instance,
    }
    return render(request, 'dashboard/edit_post.html',context)

def delete_post(request, pk):
    post = Blog.objects.get(pk=pk)
    post.delete()
    return redirect('posts')

def users(request):
    userss = User.objects.all()
    context = {
        'users': userss,
    }
    return render(request, 'dashboard/users.html',context)


def add_user(request):
    if request.method == 'POST':
        form_instance = AddUserForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('users')
        else:
            print(form_instance.errors)
    form_instance=AddUserForm()
    context = {
        'form': form_instance,
    }
    return render(request, 'dashboard/add_user.html',context)

def edit_user(request, pk):
    if request.method == 'POST':
        form_instance = EditUserForm(request.POST, instance=User.objects.get(pk=pk))
        if form_instance.is_valid():  #manager dont have to edit passwords
            form_instance.save()
            return redirect('users')
    form_instance = EditUserForm(instance=User.objects.get(pk=pk))
    context = {
        'form': form_instance,
    }
    return render(request, 'dashboard/edit_user.html',context)

def delete_user(request, pk):
    u=User.objects.get(pk=pk)
    u.delete()
    return redirect('users')