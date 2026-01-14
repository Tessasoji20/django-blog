from django.contrib import admin
from blogs.models import Category,Blog,About
from blogs.models import Sociallink,Comment

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}##slug generation
    list_display = ('title', 'category','author','status','is_featured')
    search_fields = ('id','title','category__category_name','status')
    list_editable = ('is_featured',)

class AboutAdmin(admin.ModelAdmin):
    # to allow  only single entry in the about model
    def has_add_permission(self, request):
        count=About.objects.all().count()
        if count==0:
            return True
        else:
            return False


# Register your models here.
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Sociallink)
admin.site.register(Comment)