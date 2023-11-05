from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import Product , Brand , Review


def brand_list(request):
    data = Brand.objects.all() # query --> method --> change data main query
    return render(request, 'html', {'brands': data}) # {'brands': data} --> context method(extra data) , html = template


def mydebug(request):
    data = Product.objects.select_related('brand').all()
    return render(request,'products/debug.html',{'data':data})




class ProductList(generic.ListView):
    model = Product
    paginate_by = 50


class ProductDetail(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        return context


class BrandList(generic.ListView):
    model = Brand
    paginate_by = 50


class BrandDetail(generic.ListView):
    model = Product
    template_name = 'products/brand_detail.html'

    # override main query to get products for brand comming from url 
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = super().get_queryset().filter(brand=brand)
        return queryset
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context
