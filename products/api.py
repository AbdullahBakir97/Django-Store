# views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product

@api_view(['GET',])
def product_list_api(request):
    products = Product.objects.all()
    data = ProductSerializer(products,many=True).data
    return Response({'products':data})


@api_view(['GET',])
def product_detail_api(request,id):
    product = Product.objects.get(id=id)
    data = ProductSerializer(product,context={'request':request}).data
    return Response({'product':data})




class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer