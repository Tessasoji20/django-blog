from blogs.models import Category,Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        # no slug,author options(if editor can set anyone else as author)
        fields = ['title','category','featured_image','short_description','blog_body','status','is_featured']

class AddUserForm(UserCreationForm): #usercreationfrom by default pswd1 and 2
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions']

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions']