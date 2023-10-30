from django_filters import rest_framework as filters
from .models import Product



class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['contains', ],
            'price': ['lte', 'gte', 'range'],
            'flag': ['exact'],
            'brand': ['exact'],
            'quantity': ['range'],
            
        }