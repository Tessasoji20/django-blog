from blogs.models import Category

from blogs.models import Sociallink


def get_categories(request):
    categories = Category.objects.all().order_by('created_at')
    return dict(categories=categories)

def get_social_links(request):
    social_links = Sociallink.objects.all()
    return dict(social_links=social_links)
