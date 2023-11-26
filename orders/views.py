from django.shortcuts import render , redirect
from .models import Cart , CartDetail , Order
from products.models import Product



def order_list(request):
    orders = Order.objects.all()
    return render(request,'orders/orderlist.html',{'orders':orders})





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
    checkout = ''
    return render(request, 'orders/checkout.html',{})



def process_payment(request):
    pass



def payment_success(request):
    pass



def payment_failed(request):
    pass