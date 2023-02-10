from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


from Market.forms import PaymentForm
from django.contrib import messages

from ..models import *

def view_basket(request):
    if not Basket.objects.filter(user=request.user).exists():
        basket = Basket.objects.create(user=request.user)
    basket = Basket.objects.get(user=request.user)
    basket_items = Basket_product.objects.filter(basket=basket).order_by('product_id')
    basket_total = 0
    for a in basket_items:
        basket_total += int(a.quantity) * int(a.product.price)
        
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            amount = basket_total

            # store the order in the database
            order = Order.objects.create(
                amount=amount,
                user=request.user
            )
            return redirect('buy', order_num=order.order_number)
        
    else:
        form = PaymentForm()
    # return render(request, 'payment_form.html', {'form': form})
    return render(request,  'Basket/basket.html', {"basket_items":basket_items, "basket_total":basket_total, "basket":basket, 'form':form})

@login_required
def add_basket(request, pk):
    if Basket.objects.filter(user=request.user).exists():
        basket = Basket.objects.get(user=request.user)
        product =  get_object_or_404(Product, pk=pk)
        if Basket_product.objects.filter(product=product, basket=basket).exists():
            basket_product = Basket_product.objects.get(product=product)
            if int(basket_product.quantity) >= product.quantity:
                messages.error(request, "Ошибка, нельзя набрать товаров больше, чем есть на самом деле")
            else:
                basket_items = Basket_product.objects.filter(pk = basket_product.pk, product=product, basket=basket).update(quantity = int(basket_product.quantity) + 1)
        else:
            basket_items = Basket_product.objects.create(product=product, basket=basket, quantity=1)
    else:
        basket = Basket.objects.create(user=request.user)
        product =  get_object_or_404(Product, pk=pk)
        basket_items = Basket_product.objects.create(product=product, basket=basket, quantity=1)
    return redirect('catalog')

def addition_basket(request, product, basket):
    basket_product = Basket_product.objects.get(pk=product)
    products = get_object_or_404(Product, basket_product=basket_product)
    if int(basket_product.quantity) >= products.quantity:
        messages.error(request, "Ошибка, нельзя набрать товаров больше, чем есть на самом деле")
    else:
        basket_items = Basket_product.objects.filter(pk=product, basket_id=basket).update(quantity = int(basket_product.quantity) + 1)
    return redirect("view_basket")

def subtraction_basket(request, product, basket):
    basket_product = Basket_product.objects.get(pk=product)
    if basket_product.quantity == 1:
        basket_product.delete()
    else:
        basket_items = Basket_product.objects.filter(pk=product, basket_id=basket).update(quantity = int(basket_product.quantity) - 1)
    return redirect("view_basket")