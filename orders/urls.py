from django.urls import path
from .views import add_to_cart , order_list , checkout , process_payment , payment_success , payment_failed

from .api import OrderListAPI , OrderDetailAPI , ApplyCouponAPI , CartCreateDetailDeleteAPI

app_name = 'orders'



urlpatterns = [
    path('',order_list),
    path('checkout' , checkout),
    path('checkout/payment' , process_payment),
    path('checkout/payment/success' , payment_success),
    path('checkout/payment/failed' , payment_failed),
    path('add-to-cart' , add_to_cart , name='add-to-cart'),


    # api
    path('api/<str:username>', OrderListAPI.as_view()),
    path('api/<str:username>/cart', CartCreateDetailDeleteAPI.as_view()),
    path('api/<str:username>/<int:pk>', OrderDetailAPI.as_view()),
    path('api/<str:username>/apply-coupon', ApplyCouponAPI.as_view()),
]
