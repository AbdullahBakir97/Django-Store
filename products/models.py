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
    name = models.CharField(max_length=120)
    subtitle = models.TextField(max_length=500)
    description = models.TextField(max_length=100000)
    image = models.ImageField(upload_to='products')
    price = models.FloatField()
    flag = models.CharField(max_length=10)
    brand = ''
    sku = models.CharField(max_length=12)
    quantity = models.IntegerField()

