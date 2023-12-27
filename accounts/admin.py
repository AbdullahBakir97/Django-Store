from django.contrib import admin
from .models import DeliveryAddress , Profile , Phones


admin.site.register(Profile)
admin.site.register(Phones)
admin.site.register(DeliveryAddress)

