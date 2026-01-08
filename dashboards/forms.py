from blogs.models import Category,Blog
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