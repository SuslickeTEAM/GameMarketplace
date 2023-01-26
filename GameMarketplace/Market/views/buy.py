from yookassa import Configuration, Payment
import uuid
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404


from ..models import *
import time


def BuyProduct(request):
    Configuration.account_id = 979061
    Configuration.secret_key = 'test_SwADBtkw-F0m3cQegKG_qxgHvzRDI8JM2GParX__wVg'
    basket = Basket.objects.get(user=request.user)
    basket_total = 0
    basket_items = Basket_product.objects.filter(basket=basket).order_by('product_id')
    for a in basket_items:
        basket_total += int(a.quantity) * int(a.product.price)
        
    uuids = uuid.uuid4()
    payment = Payment.create({
    "amount": {
        "value": f"{basket_total}",
        "currency": "RUB"
    },
    "confirmation": {
        "type": "redirect",
        "return_url": f"http://127.0.0.1:8000/basket/buy/{basket.id}/confirm-buy/"
    },
    "capture": True,
    "description": f"Заказ {basket.id}"}, uuids)
    
    confirm_id = payment.id
    
    return redirect(f'https://yoomoney.ru/checkout/payments/v2/contract?orderId={confirm_id}')
    

def BuyConfirm(request, pk):
    Configuration.account_id = 979061
    Configuration.secret_key = 'test_SwADBtkw-F0m3cQegKG_qxgHvzRDI8JM2GParX__wVg'
    params = {'limit': 3, 'status': 'succeeded'}
    payment_list = Payment.list(params)
    
    basket_id = Basket.objects.get(user=request.user)
    
    sell = False
    
    for items in payment_list.items:
        if items.description == f"Заказ {basket_id.id}" and basket_id.id == pk:
            if items.status == "succeeded":
                error = False
                basket_items = Basket_product.objects.filter(basket=basket_id).order_by('product_id')
                # Add buy in history
                return render(request, 'Basket/confirm.html', {'basket_items': basket_items, 'error':error})
            else:
                error = True
                return render(request, 'Basket/confirm.html', {'basket_items': basket_items, 'error':error})
            
    
    if sell:
        basket_id.delete()
    
    
    raise Http404("Произошла ошибка" )