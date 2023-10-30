# form
from rest_framework import serializers
from .models import Product , Brand , Review , ProductImages


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'




class BrandSerializer(serializers.ModelSerializer):
     class Meta:
        model = Brand
        fields = '__all__'