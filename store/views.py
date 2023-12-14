from django.shortcuts import render , get_object_or_404
from .models import Product
from category.models import Category
from django.db.models import Count
from django.views.generic import ListView 
from django.db.models.query_utils import Q
from taggit.models import Tag
from django.core.paginator import Paginator


# Create your views here.
def store(request , category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 12)  # Show 25 contacts per page.

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products,2)  # Show 25 contacts per page.

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        product_count = products.count()
    product = Product.objects.all().filter(is_available=True).order_by('id')
    all_product_count = product.count()
    tags = Tag.objects.all()

    context = {
        'products':page_obj,
        'product_count': product_count,
        'all_product_count':all_product_count,
        'tags':tags,
    }
    return render(request , 'product/store.html' , context)

class Search(ListView):
    model = Product
    template_name = 'tags/store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = Product.objects.all()
        context["all_product_count"] = Product.objects.all().count()
        context["tags"] = Tag.objects.all()

        return context
    def get_queryset(self) :
        q = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(name__icontains = q) |
            Q(description__icontains = q))        
        return object_list

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
    paginate_by = 2
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