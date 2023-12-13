from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField( max_length=50 , unique=True)
    slug = models.SlugField(max_length=50 , unique=True)
    description = models.TextField( max_length=2000 , blank=True)
    image = models.ImageField( upload_to='product_img')
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey("category.Category",related_name=("product"), verbose_name=("category product"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateField( auto_now=True)

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.category.slug ,self.slug])


    def __str__(self):
        return self.name