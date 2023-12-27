from django.contrib import admin
from .models import Product, Brand, ProductImages, Review
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImages


class ProductAdmin(TranslationAdmin):
    list_display = [ 'id', 'name','sku','flag','price','quantity']
    list_filter = ['flag','brand']
    search_fields = ['name','subtitle','description']
    inlines = [ProductImageInline]


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Review)