from django.shortcuts import render, get_object_or_404, redirect

from ..models import Category
from ..filters import CategoryFilter



# def Fielter_category(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request, 'catalog.html',{'category': category,'categories': categories,'products': products,'current_category': category.slug})

def category_view(request):
    category = Category.objects.all()
    category_filter = CategoryFilter(request.GET, queryset=category)
    return render(request, "Market/catalog.html", {"category_filter": category_filter})
