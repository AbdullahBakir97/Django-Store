from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User,related_name='user_profile',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='accounts',null=True,blank=True)
    code = models.CharField(max_length=10,default=generate_code)

    def __str__(self):
        return str(self.user)
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user = instance
        )

    


PHONE_TYPES = (
    ('Primary','Primary'),
    ('Secondary','Secondary')
)
class Phones(models.Model):
    user = models.ForeignKey(User,related_name='user_phone',on_delete=models.CASCADE)
    type = models.CharField(max_length=12,choices=PHONE_TYPES)
    phone = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.type} - {self.phone}"
    

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


    def __str__(self):
        return f"{self.type} - {self.address}"