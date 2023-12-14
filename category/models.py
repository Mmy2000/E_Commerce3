from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(unique=True, max_length=50)
    slug = models.SlugField(unique=True, max_length=100)
    image = models.ImageField( upload_to='cat_img' , blank=True)
    clas = models.CharField(max_length=50 ,blank=True ,null=True)
    description = models.TextField(max_length=10000,blank=True ,null=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('product_by_category',args=[self.slug])

    def __str__(self):
        return str(self.category_name)
    
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(unique=True, max_length=50)
    slug = models.SlugField(unique=True, max_length=100)
    image = models.ImageField( upload_to='subcat_img' , blank=True)
    description = models.TextField(max_length=10000,blank=True ,null=True)

    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'


    def __str__(self):
        return str(self.subcategory_name)
