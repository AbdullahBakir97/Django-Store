from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import Product , Brand , Review


def brand_list(request):
    data = Brand.objects.all() # query --> method --> change data main query
    return render(request, 'html', {'brands': data}) # {'brands': data} --> context method(extra data) , html = template



class ProductList(generic.ListView):
    model = Product



class ProductDetail(generic.DetailView):
    model = Product


class BrandList(generic.ListView):
    model = Brand


class BrandDetail(generic.ListView):
    model = Product
    template_name = 'products/brand_detail.html'

    # override main query to get products for brand comming from url 
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = super().get_queryset().filter(brand=brand)
        return queryset
    

    def get_context_data(self):
        context = super().get_context_data()
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context
