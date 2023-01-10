from django.shortcuts import render, get_object_or_404, redirect

from ..models import *

def view_basket(request):
    basket = Basket.objects.get(user=request.user)
    basket_items = Basket_product.objects.filter(basket=basket)
    return render(request,  'Basket/basket.html', {"basket_items":basket_items})

def add_basket(request, pk):
    if Basket.objects.filter(user=request.user).exists():
        basket = Basket.objects.get(user=request.user)
        product =  get_object_or_404(Product, pk=pk)
        if Basket_product.objects.filter(product=product, basket=basket).exists():
            basket_product = Basket_product.objects.get(product=product)
            basket_items = Basket_product.objects.filter(pk = basket_product.pk, product=product, basket=basket).update(quantity = int(basket_product.quantity) + 1)
        else:
            basket_items = Basket_product.objects.create(product=product, basket=basket, quantity=1)
    else:
        basket = Basket.objects.create(user=request.user)
        product =  get_object_or_404(Product, pk=pk)
        basket_items = Basket_product.objects.create(product=product, basket=basket, quantity=1)
    return redirect("view_basket")