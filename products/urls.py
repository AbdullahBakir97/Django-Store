from django.urls import path
from .views import ProductList , ProductDetail



urlpatterns = [
    path('',ProductList.as_view()) ,
    path('<slug:slug>',ProductList.as_view()) ,
]