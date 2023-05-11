from django.contrib import admin
from .models import Element, Product, Product_Element, Product_type


admin.site.register(Element)
admin.site.register(Product)
admin.site.register(Product_Element)
admin.site.register(Product_type)
