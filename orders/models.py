from django.db import models
from django.utils import timezone
import datetime

class Order(models.Model):
    pass



class OrderDetail(models.Model):
    pass



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


