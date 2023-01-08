from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import Http404

from ..models import *

@login_required
def catalog(request):
    products = Product.objects.all()
    return render(request, "Market/Catalog.html", {"products": products})
