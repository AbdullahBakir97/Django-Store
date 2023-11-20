from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

import datetime


ORDER_STATUS = (
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
)


class Order(models.Model):
    user = models.ForeignKey(User,related_name='order_user',on_delete=models.SET_NULL , null=True,blank=True)
    code = models.CharField(max_length=10)
    status = models.CharField(max_length=15 , choices=ORDER_STATUS,default='Recieved')
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True,blank=True)
    delivery_location = ''
    coupon = models.ForeignKey('Coupon',related_name='order_coupon',on_delete=models.SET_NULL , null=True,blank=True)
    order_total_discount = models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.user)

class OrderDetail(models.Model):
    product = ''
    quantity = ''
    brand = ''
    price = ' '



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


