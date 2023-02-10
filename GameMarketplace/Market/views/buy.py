from yookassa import Configuration, Payment
import uuid
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

Configuration.account_id = 979061
Configuration.secret_key = 'test_SwADBtkw-F0m3cQegKG_qxgHvzRDI8JM2GParX__wVg'

from ..models import *


def buy_product(request, order_num):
    order = Order.objects.filter(order_number=order_num).first()
    
    uuids = uuid.uuid4()
    payment = Payment.create({
    "amount": {
        "value": f"{order.amount}",
        "currency": "RUB"
    },
    "confirmation": {
        "type": "redirect",
        "return_url": f"http://127.0.0.1:8000/basket/buy/{order.order_number}/confirm-buy/"
    },
    "capture": True,
    "description": f"Заказ {order.id}"}, uuids)
    
    payment_id = payment.id
    order.payment_id = payment_id
    order.status = 'processing'
    order.save()
    
    return redirect(f'https://yoomoney.ru/checkout/payments/v2/contract?orderId={payment_id}')
    

def buy_confirm(request, pk):
    # params = {'limit': 3, 'status': 'succeeded'}
    # payment_list = Payment.list(params)
    
    # basket_id = Basket.objects.get(user=request.user)
    order = Order.objects.filter(order_number=pk).first()
    payment = Payment.find_one(order.payment_id)
    
    if payment.description == f"Заказ {order.id}" and order.order_number == pk and request.user == order.user:
        if payment.status == "succeeded":
            error = False
            order.status = 'paid'
            order.save()
            basket = get_object_or_404(Basket, user=request.user)
            basket_items = Basket_product.objects.filter(basket=basket).order_by('product_id')
            # if PurchaseHistory.objects.get(user=request.user).exists():
            #     for item in basket_items:
            #         purchase_history.product.add(Product.objects.get(pk=item.product.pk))
            # else:
            
            for item in basket_items:
                product = Product.objects.get(pk=item.product.pk)
                if PurchaseHistory.objects.filter(order_number=order, product=product).exists():
                    break
                else:
                    PurchaseHistory.objects.create(order_number=order, user=request.user, product=product, quantity=item.quantity)
                    
                purchase = PurchaseHistory.objects.get(order_number=order, product=product)
                
                
                product_detail = ProductDetail.objects.filter(user__isnull=True, product=product)[:item.quantity]
                
                for pr_det in product_detail:
                    purchase.details.add(pr_det)
                    pr_det.user = request.user
                    pr_det.save()
                # flag = False
                # for details_history in PurchaseHistory.objects.all():
                #     for detail in details_history.details.all():
                #         for products_details in ProductDetail.objects.filter(product=product):
                #             if products_details in detail:
                #                 flag = True
                
                # if flag == False:    
                #     for products_details in ProductDetail.objects.filter(product=product)[:item.quantity]:
                #         purchase.details.add(products_details)
                            
                # extra_product = []
                # extra_history = []
                
                # for extra in list(product.extra_data['accounts']):
                #     for y in list(product.extra_data['accounts'])[:item.quantity]:
                #         extra_history.append(product.extra_data['accounts'][y])
                #     if not product.extra_data['accounts'][extra] in extra_history:
                #         extra_product.append(product.extra_data['accounts'][extra])
                        
                        
                # first, *history = extra_history
                # second, *products = extra_product
                # purchase.update(extra_data=first + history)
                
                # product.extra_data = second + extra_product
                if product.quantity - item.quantity == 0:
                    product.is_sold = True
                else:
                    product.quantity = product.quantity - item.quantity
                product.save()
            # Add buy in history

            basket.delete()
            #     purchase_item = PurchaseHistoryQuantity.objects.create(purchase=purchase_history, product=Product.objects.get(pk=item.product.pk), quantity=item.quantity)
            #     print(item)
            #     purchase_history.product.add(purchase_item)
            #     purchase_history.save()
            
            return redirect('profile')
        else:
            error = True
            return render(request, 'Basket/confirm.html', {'basket_items': basket_items, 'error':error})
    
    
    raise Http404("Произошла ошибка" )