from django.urls import path
from .views import ProductList , ProductDetail , BrandList



urlpatterns = [
    path('',ProductList.as_view()) ,
    path('<slug:slug>',ProductList.as_view()) ,

    path('brands/' , BrandList.as_view()),
]

