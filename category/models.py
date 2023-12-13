from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(unique=True, max_length=50)
    slug = models.SlugField(unique=True, max_length=100)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return str(self.category_name)
    
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(unique=True, max_length=50)
    slug = models.SlugField(unique=True, max_length=100)
    image = models.ImageField( upload_to='subcat_img' , blank=True)

    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'


    def __str__(self):
        return str(self.subcategory_name)
