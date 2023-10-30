# views
from rest_framework import generics , filters
from django_filters.rest_framework import DjangoFilterBackend 
from .serializers import ProductSerializer , BrandSerializer
from .models import Product , Brand
from .mypagination import MyPagination
from .myfilter import ProductFilter





class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend , filters.SearchFilter , filters.OrderingFilter]
    filterset_fields = ['flag', 'brand']
    search_fields = ['name', 'subtitle', 'description']
    ordering_fields = ['price', 'quantity']
    filterset_class = ProductFilter


class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    pagination_class = MyPagination



class BrandDetailAPI(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer