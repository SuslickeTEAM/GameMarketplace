from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import Http404

from ..models import *
from ..filters import CategoryFilter

@login_required
def catalog(request):
    products = Product.objects.all()
    category = Category.objects.all()
    products_filter = CategoryFilter(request.GET, queryset=products)
    # category_filter = CategoryFilter(request.GET, queryset=products)
    return render(request, "Market/catalog.html", {"products_filter": products_filter})


def product_info(request, pk):
    products_info = get_object_or_404(Product_info, pk=pk)
    product = get_object_or_404(Product, pk=pk)
    return render(request, "Market/Product_info.html", {"products_info": products_info, "product": product})
