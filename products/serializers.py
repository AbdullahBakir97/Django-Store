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
    avg_rate = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'

    def get_review_count(self,object):
        review_count = object.product_review.all().count()
        return review_count


    def get_avg_rate(self,object):
        total = 0
        reviews = object.product_review.all()
        for r in reviews:
            total += r.rate

        if len(reviews) > 0:
            return total/len(reviews)
        else:
            return 0

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