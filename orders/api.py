from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
import datetime

from .models import Cart , CartDetail , Order , OrderDetail 
from .serializers import CartSerializer , CartDetailSerializer , OrderSerializer , OrderDetailSerializer
from settings.models import DeliveryFee


class OrderListAPI(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    # get_queryset , list
    def list(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        queryset = self.get_queryset().filter(user=user)  
        data = OrderSerializer(queryset,many=True).data
        return Response({'orders':data})
    


class OrderDetailAPI(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()