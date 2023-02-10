from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import Http404
from django.views import View
from django.contrib.messages import get_messages
from ..models import *


def catalog(request):
    products = Product.objects.all().exclude(is_sold=True)
    category = Category.objects.all()
    special = SpecialOffer.objects.all()
    
    return render(request, "Market/catalog.html", {"category": category, 'products': products, 'specialoffers': special, 'body_class': 'catalog'})
    
    
def catalog_filter(request, *args, **kwargs):
    products = Product.objects.filter(category__in=request.GET.getlist('category')).exclude(is_sold=True)
    category = Category.objects.all()
    return render(request, "Market/catalog.html", {"category": category, 'products': products})


def index(request):
    special = SpecialOffer.objects.filter(title="Index")
    return render(request, "Market/index.html", {'body_class': 'black'})