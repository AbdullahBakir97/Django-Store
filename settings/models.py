from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company')
    call_us = models.CharField(max_length=100)
    email_us = models.CharField(max_length=100)
    subtitle = models.TextField(max_length=500)
    fb_link = models.URLField(null=True,blank=True)
    youtube_link = models.URLField(null=True,blank=True)
    insta_link = models.URLField(null=True,blank=True)
    linkedin_link = models.URLField(null=True,blank=True)
    emails = models.TextField(max_length=100)
    phones = models.TextField(max_length=100)
    address = models.TextField(max_length=150)
    android_link = models.URLField(null=True,blank=True)
    ios_link = models.URLField(null=True,blank=True)


    def __str__(self):
        return self.name