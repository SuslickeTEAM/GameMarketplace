from django.shortcuts import render, get_object_or_404, redirect

from ..models import *

def view_basket(request):
    basket = Basket.objects.get(user=request.user)
    basket_items = Basket_product.objects.filter(basket=basket)
    basket_total = 0
    for a in basket_items:
        basket_total += int(a.quantity) * int(a.product.price)
    return render(request,  'Basket/basket.html', {"basket_items":basket_items, "basket_total":basket_total, "basket":basket})

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

def addition_basket(request, product, basket):
    basket_product = Basket_product.objects.get(pk=product)
    basket_items = Basket_product.objects.filter(pk=product, basket_id=basket).update(quantity = int(basket_product.quantity) + 1)
    return redirect("view_basket")

def subtraction_basket(request, product, basket):
    basket_product = Basket_product.objects.get(pk=product)
    if basket_product.quantity == 1:
        basket_product.delete()
    else:
        basket_items = Basket_product.objects.filter(pk=product, basket_id=basket).update(quantity = int(basket_product.quantity) - 1)
    return redirect("view_basket")