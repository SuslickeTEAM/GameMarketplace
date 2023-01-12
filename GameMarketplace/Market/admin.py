from django.contrib import admin

from .models import Basket, Product, Basket_product, Category, Product_info


admin.site.register(Basket)
admin.site.register(Basket_product)
admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    
@admin.register(Product_info)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'title', 'description')