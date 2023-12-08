# views
from rest_framework import generics , filters
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductListSerializer , ProductDetailSerializer , BrandListSerializer , BrandDetailSerializer
from .models import Product , Brand
from .mypagination import MyPagination
from .myfilter import ProductFilter





class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend , filters.SearchFilter , filters.OrderingFilter]
    filterset_fields = ['flag', 'brand']
    search_fields = ['name', 'subtitle', 'description']
    ordering_fields = ['price', 'quantity']
    filterset_class = ProductFilter
    #permission_classes = [IsAuthenticated]


class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer



class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
    pagination_class = MyPagination



class BrandDetailAPI(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer