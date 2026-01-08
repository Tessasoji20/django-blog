from django.http import HttpResponse
from django.shortcuts import render,redirect
from blogs.models import Category,Blog
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from blogs.models import About
from django.contrib import messages
from blog_main.forms import RegisterForm


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

def register(request):
    if request.method == 'POST':
        form_instance = RegisterForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('register')
        else:
            print(form_instance.errors)
    else:
            form_instance=RegisterForm()
    context={
        'form':form_instance,
    }
    return render(request, 'register.html',context)

def userlogin(request):
    if request.method == 'GET':
         form_instance = AuthenticationForm()
         context = {
             'form':form_instance,
         }
         return render(request, 'login.html',context)
    if request.method == 'POST':
         form_instance = AuthenticationForm(request,data=request.POST)
         if form_instance.is_valid():
             data = form_instance.cleaned_data
             u=data['username']
             p=data['password']
             user = authenticate(username=u, password=p)
             if user:
                 login(request,user)
                 return redirect('dashboard')
             else:
                 messages.error(request, 'Username or Password is incorrect')
                 # return redirect('users:userlogin')
                 # if form instance is invalid
                 return render(request, 'login.html', {'form': form_instance})


def userlogout(request):
    logout(request)
    return redirect('home')

