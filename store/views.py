from django.shortcuts import render , get_object_or_404
from .models import Product
from category.models import Category
from django.db.models import Count
from django.views.generic import ListView 
from django.db.models.query_utils import Q
from taggit.models import Tag

# Create your views here.
def store(request , category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        product_count = products.count()
    product = Product.objects.all().filter(is_available=True).order_by('id')
    all_product_count = product.count()
    tags = Tag.objects.all()

    context = {
        'products':products,
        'product_count': product_count,
        'all_product_count':all_product_count,
        'tags':tags,
    }
    return render(request , 'product/store.html' , context)

def product_detail(request , category_slug , product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        related = Product.objects.filter(category=single_product.category)
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
        'related':related,
    }
    return render(request , 'product/product_detail.html', context)

class ProductByTags(ListView):
    model = Product
    template_name = 'tags/store.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = Product.objects.all()
        context["all_product_count"] = Product.objects.all().count()
        context["tags"] = Tag.objects.all()

        return context


    def get_queryset(self) :
        slug = self.kwargs['slug']
        object_list = Product.objects.filter(
            Q(tags__name__icontains = slug)
        )
        return object_list