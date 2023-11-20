from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from products.models import Product
import datetime
from utils.generate_code import generate_code
from accounts.models import DeliveryAddress

ORDER_STATUS = (
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
)


class Order(models.Model):
    user = models.ForeignKey(User,related_name='order_user',on_delete=models.SET_NULL , null=True,blank=True)
    code = models.CharField(max_length=10,default=generate_code)
    status = models.CharField(max_length=15 , choices=ORDER_STATUS,default='Recieved')
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True,blank=True)
    delivery_location = models.ForeignKey(DeliveryAddress,related_name='delivery_address',on_delete=models.SET_NULL,null=True,blank=True)
    coupon = models.ForeignKey('Coupon',related_name='order_coupon',on_delete=models.SET_NULL , null=True,blank=True)
    order_total_discount = models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.user)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name='order_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='orderdetail_product',on_delete=models.SET_NULL , null=True,blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()


CART_STATUS = (
    ('Inprogress','Inprogress'),
    ('Completed','Completed'),
)

class Cart(models.Model):
    user = models.ForeignKey(User,related_name='cart_user',on_delete=models.SET_NULL , null=True,blank=True)
    status = models.CharField(max_length=15 , choices=CART_STATUS,default='Recieved')
    coupon = models.ForeignKey('Coupon',related_name='cart_coupon',on_delete=models.SET_NULL , null=True,blank=True)
    cart_total_discount = models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.user)

class CartDetail(models.Model):
    cart = models.ForeignKey(Cart,related_name='cart_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='cartdetail_product',on_delete=models.SET_NULL , null=True,blank=True)
    quantity = models.IntegerField()
    total = models.FloatField()


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    start_date = models.DateField(null=True,blank=True , default=timezone.now)
    end_date = models.DateField(null=True,blank=True , )
    quantity = models.IntegerField()
    discount = models.FloatField()

    def __str__(self):
        return self.code

    def save(self,*args, **kwargs):
        week = datetime.timedelta(days=7)
        self.end_date = self.start_date + week
        super(Coupon,self).save(*args, **kwargs)


