from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

FLAG_TYPES =(
    ('Sale','Sale'),
    ('New','New'),
    ('Feature','Feature'),
)



class Product(models.Model):
    name = models.CharField(_('Name'),max_length=120)
    subtitle = models.TextField(_('Subtitle'),max_length=500)
    description = models.TextField(_('Description'),max_length=100000)
    image = models.ImageField(_('Image'),upload_to='products')
    price = models.FloatField(_('Price'))
    flag = models.CharField(_('Flag'),max_length=10,choices=FLAG_TYPES)
    brand = models.ForeignKey('Brand',verbos_name=_('Brand'),related_name='product_brand',on_delete=models.SET_NULL,null=True,blank=True)
    sku = models.CharField(_('SKU'),max_length=12)
    quantity = models.IntegerField(_('Quantity'))
    tags = TaggableManager()
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.name


    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Product,self).save(*args, **kwargs)

class ProductImages(models.Model):
    product = models.ForeignKey(Product,related_name='product_images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productimages')

    def __str__(self):
        return str(self.product)

class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='brands')

    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Brand,self).save(*args, **kwargs)


class Review(models.Model):
    user = models.ForeignKey(User,related_name='review_author',on_delete=models.SET_NULL,null=True,blank=True)
    Product = models.ForeignKey(Product,related_name='Product_review',on_delete=models.CASCADE)
    rate = models.IntegerField()
    feedback = models.TextField(max_length=500)
    created_at = models.TimeField(default=timezone.now)

    def __str__(self):
        return str(self.user)

