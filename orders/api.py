from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
import datetime

from .models import Cart , CartDetail , Order , OrderDetail , Coupon
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


class ApplyCouponAPI(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart = Cart.objects.get(user=request.user , status='Inprogress')
        cart_detail = CartDetail.objects.filter(cart=cart)
        delivery_fee = DeliveryFee.objects.last().fee
        sub_total = cart.cart_total()
        coupon = Coupon.objects.get(code=request.data['coupon_code'])

        if coupon and coupon.quantity > 0 :
            today = datetime.datetime.today().date()
            if today >= coupon.start_date and today < coupon.end_date :
                coupon_value = sub_total / 100*coupon.discount
                sub_total = sub_total - coupon_value
                total = sub_total + delivery_fee

                cart.coupon = coupon
                cart.cart_total_discount = sub_total
                cart.save()

                return Response({'message':'coupon code applied successfully'})
            else:
                return Response({'message':'coupon code date is not valid '})
            
        
        return Response({'message':'coupon not found or coupon ended '})
    


class CartCreateDetailDeleteAPI(generics.GenericAPIView):

    def get(self,request,*args, **kwargs):
        """ get or create cart """
        user = User.objects.get(username=self.kwargs['username'])
        cart , created = Cart.objects.get_or_create(user=request.user , status='Inprogress')
        data = CartSerializer(cart).data
        return Response({'cart':data})

    def post(self,request,*args, **kwargs):
        """ add or update """
        user = User.objects.get(username=self.kwargs['username'])


    def delete(self,request,*args, **kwargs):

        user = User.objects.get(username=self.kwargs['username'])
        cart = Cart.objects.get(user=request.user , status='Inprogress')
        product = CartDetail.objects.get(id=request.data['product_id'])

        product.delete()
        return Response({'massage':'item was deleted successfuly'})