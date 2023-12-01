from django.shortcuts import render , redirect
from .models import Cart , CartDetail , Order , Coupon
from products.models import Product
from settings.models import DeliveryFee
import datetime


def order_list(request):
    orders = Order.objects.filter(user=request.user)
    cart = Cart.objects.get(user=request.user , status='Inprogress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    delivery_fee = DeliveryFee.objects.last().fee

    sub_total = cart.cart_total()
    discount = 0
    total = sub_total + delivery_fee

    return render(request,'orders/orderlist.html',{
        'orders':orders ,
        'cart_detail': cart_detail ,
        'delivery_fee': delivery_fee ,
        'sub_total': sub_total ,
        'discount': discount ,
        'total': total ,

    })





def add_to_cart(request):
    product = Product.objects.get(id=request.POST['product_id'])
    quantity = int(request.POST['quantity'])

    cart = Cart.objects.get(user=request.user , status='Inprogress')
    cart_detail,created = CartDetail.objects.get_or_create(cart=cart , product=product)

    cart_detail.quantity = quantity
    cart_detail.total = round(quantity * product.price,2)
    cart_detail.save()

    return redirect(f"/products/{product.slug}")



def checkout(request):
    cart = Cart.objects.get(user=request.user , status='Inprogress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    delivery_fee = DeliveryFee.objects.last().fee
    sub_total = cart.cart_total()

    if request.method == 'POST':
        code = request.POST['coupon_code']
        coupon = Coupon.objects.get(code=code)

        if coupon and coupon.quantity > 0 :
            today = datetime.datetime.today().date()
            if today >= coupon.start_date and today < coupon.end_date :
                coupon_value = sub_total / 100*coupon.discount
                #sub_total = cart.cart_total() - coupon_value
                sub_total = sub_total - coupon_value
                total = sub_total + delivery_fee

                cart.coupon = coupon
                cart.cart_total_discount = sub_total
                cart.save()

                return render(request, 'orders/checkout.html',{
                    'cart_detail': cart_detail ,
                    'delivery_fee': delivery_fee ,
                    'sub_total': sub_total ,
                    'discount': coupon_value ,
                    'total': total ,
                })
    
    discount = 0
    total = sub_total + delivery_fee


    
    return render(request, 'orders/checkout.html',{
        'cart_detail': cart_detail ,
        'delivery_fee': delivery_fee ,
        'sub_total': sub_total ,
        'discount': discount ,
        'total': total ,
    })



def process_payment(request):
    pass



def payment_success(request):
    pass



def payment_failed(request):
    pass