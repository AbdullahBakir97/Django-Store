# views
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
