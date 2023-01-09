from django.shortcuts import render

from ..models import *

def view_basket(request):
    basket = Basket.objects.get(user=request.user)
    basket_items = Basket_product.objects.filter(basket=basket)
    return render(request,  'Basket/basket.html', {"basket_items":basket_items})