from django.contrib import admin

from .models import *


admin.site.register(Basket)
admin.site.register(Basket_product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Profile)
admin.site.register(SpecialOffer)
admin.site.register(PurchaseHistory)

admin.site.register(ProductDetail)
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'category', 'admin_photo')
#     readonly_fields= ('admin_photo',)
    
class ChildInline(admin.TabularInline):
    model = ProductDetail

@admin.register(Product)
class ParentAdmin(admin.ModelAdmin):
    inlines = [ChildInline]
    list_display = ('name', 'price', 'category', 'admin_photo')
    readonly_fields= ('admin_photo',)
    
    
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     inlines = [ProductDetail]
#     list_display = ('name', 'price', 'category', 'admin_photo')
#     readonly_fields= ('admin_photo',)
#     class Meta:
#         model = Product
        

