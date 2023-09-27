from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=120)
    subtitle = models.TextField(max_length=550)
    description = models.TextField(max_length=100000)
    image = models.ImageField(upload_to='products')
    price = models.FloatField()
    flag = models.CharField(max_length=10)
    brand = ''
    sku = models.CharField(max_length=12)
    quantity = models.IntegerField()

