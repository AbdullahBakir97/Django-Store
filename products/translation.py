from modeltranslation.translator import translator, TranslationOptions
from .models import Product

class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'subtitle')

translator.register(Product, ProductTranslationOptions)