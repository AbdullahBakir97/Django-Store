from django.db import models
from django.contrib.auth.models import User



ADDRESS_TYPE = (
    ('Home','Home'),
    ('Office','Office'),
    ('Bussines','Bussines'),
    ('Academy','Academy'),
    ('Other','Other'),
)

class DeliveryAddress(models.Model):
    user = models.ForeignKey(User,related_name='user_address',on_delete=models.CASCADE)
    type = models.CharField(max_length=20,choices=ADDRESS_TYPE)
    address = models.TextField(max_length=300)
