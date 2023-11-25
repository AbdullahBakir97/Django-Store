from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import Product , Brand , Review
from django.db.models import Q , Value , F
from django.db.models.aggregates import Count , Min , Max , Avg , Sum
from django.views.decorators.cache import cache_page

def brand_list(request):
    data = Brand.objects.all() # query --> method --> change data main query
    return render(request, 'html', {'brands': data}) # {'brands': data} --> context method(extra data) , html = template


@cache_page(60 * 15)
def mydebug(request):
    #data = Product.objects.filter(price__gte=90)     # gte = more than or equall
    #data = Product.objects.filter(price__lte=90)     # lte = lees than or equall
    #data = Product.objects.filter(price__range=(10,90))     # range between tow values
    #data = Product.objects.filter(brand__name='Daniel Jackson')     # get product with brand name by = .... or contains ....
    #data = Product.objects.filter(brand__id__gt=20)     # get product with barnd id 
    #data = Product.objects.filter(name__startswith='William')     # get product name starts with ....
    #data = Product.objects.filter(name__endswith='Keith')     # get product name ends  with ....
    #data = Product.objects.filter(name__isnull = True)     # when a column has no value 
    #data = Product.objects.filter(name__endswith='Keith' , price__gte=90)     # more specific filters

    # data = Product.objects.filter(       # Q lockup uses in search only
    #     Q(name__startswith='Keith') or
    #     Q(price__gte=90)
    # )

    #data = Product.objects.all().order_by('name')     # ordering by name or price default: (Ascending) or Descending by adding ('-price') , or else ordering 
    #data = Product.objects.all().order_by('name' , '-price')     # more specific ordering 
    #data = Product.objects.all().order_by('name')[0]     # ordering by name and get the first one only or last by [-1] or any []
    #data = Product.objects.all().earliest('name')     # ordering by name and get the first one only automatic
    #data = Product.objects.all().latest('name')     # ordering by name and get the last one only automatic

    #data = Product.objects.all()[:10]     # get first 10 only

    #data = Product.objects.values('name' , 'price')     # return the value column in a tuple to reduce: (lodeing or returend querys) , in html nothing well be shown if value not returend here 
    #data = Product.objects.only('name' , 'price')     # returen specific value to reduce: (lodeing or returend querys) , but everything mentioned in html as value will be returned also when it's not returned here this well return to much (querys)! 
    #data = Product.objects.defer('name' , 'price')     # returen all values except mentioned : name & price , but everything mentioned in html as value will be returned also when it's not returned here this well return to much (querys)!
    
    #data = Product.objects.select_related('brand').all()     # when using foreignkey or one-to-one
    #data = Product.objects.prefetch_related('brand').all()     # when using many-to-many

    # aggregation func : min - max - sum - avg - count
    #data = Product.objects.aaggregate(myavg = Avg('price')) # myavg name want to show by default django show relation name 
    #data = Product.objects.aggregate(Count('quantity'))
    #data = Product.objects.aggregate(Count('id'))
    #data = Product.objects.aggregate(sum('quantity'))
    #data = Product.objects.aggregate(Min('price'))
    #data = Product.objects.aggregate(Max('price'))


    #data = Product.objects.annotate(is_new=Value(True))     # is_new= name , Value will add new column when data return from database , the new column will not be added to database 
    #data = Product.objects.annotate(price_with_tax=F('price')*1.25)     # price_with_tax = name , F to add and handel column from database and add a mathematical eqution on it when data return from data base , the new column will not be added to database

    data = Product.objects.all()

    return render(request,'products/debug.html',{'data':data})




class ProductList(generic.ListView):
    model = Product
    paginate_by = 50


class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
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
