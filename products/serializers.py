# form
from rest_framework import serializers
from .models import Product , Brand , Review , ProductImages


class BrandSerializer(serializers.ModelSerializer):
     class Meta:
        model = Brand
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    review_count = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'

    def get_review_count(self,object):
        review_count = object.product_review.all().count()
        return review_count 


class ProductDetailSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    class Meta:
        model = Product
        fields = '__all__'




class BrandListSerializer(serializers.ModelSerializer):
     class Meta:
        model = Brand
        fields = '__all__'




class BrandDetailSerializer(serializers.ModelSerializer):
     class Meta:
        model = Brand
        fields = '__all__'