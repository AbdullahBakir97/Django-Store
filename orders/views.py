from django.shortcuts import render , redirect
from .models import Cart , CartDetail
from products.models import Product




def add_to_cart(request):
    product = Product.objects.get(id=request.POST['product_id'])
    quantity = int(request.POST['quantity'])

    cart = Cart.objects.get(user=request.user , status='Inprogress')
    cart_detail,created = CartDetail.objects.get_or_create(cart=cart , product=product)

    cart_detail.quantity = quantity
    cart_detail.total = round(quantity * product.price,2)
    cart_detail.save()

    return redirect(f"/products/{product.slug}")