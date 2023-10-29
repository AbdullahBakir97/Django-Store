from django.urls import path
from .views import ProductList , ProductDetail , BrandList , BrandDetail
from .api import   ProductListAPI , ProductDetailAPI


urlpatterns = [
    path('',ProductList.as_view()) ,
    path('<slug:slug>',ProductDetail.as_view()) ,

    path('brands/' , BrandList.as_view()),
    path('brands/<slug:slug>' , BrandDetail.as_view()),

    # api
    path('api/list' , ProductListAPI.as_view()),
    path('api/list/<int:pk>' , ProductDetailAPI.as_view()),
]

