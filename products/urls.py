from django.urls import path
from .views import mydebug , ProductList , ProductDetail , BrandList , BrandDetail
from .api import   ProductListAPI , ProductDetailAPI , BrandListAPI , BrandDetailAPI


urlpatterns = [
    path('debug' , mydebug),
    path('' , ProductList.as_view()) ,
    path('<slug:slug>', ProductDetail.as_view()) ,

    path('brands/' , BrandList.as_view()),
    path('brands/<slug:slug>' , BrandDetail.as_view()),

    # api
    path('api/list' , ProductListAPI.as_view()),
    path('api/list/<int:pk>' , ProductDetailAPI.as_view()),
    path('api/list/brands' , BrandListAPI.as_view()),
    path('api/list/brands/<int:pk>' , BrandDetailAPI.as_view()),
]

