from .models import Category
from django.db.models import Count


def menu_links(request):
    links = Category.objects.all().annotate(products_count=Count('product'))[:10]
    return dict(links=links)