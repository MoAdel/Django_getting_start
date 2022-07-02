from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.

def detail(request, id):
    #product = Product.objects.get(pk=id)
    product = get_object_or_404(Product,pk=id)
    return render(request, "product/detail.html", {"product": product})


def product_list(request):
    return render(request, "product/product_list.html", {"products": Product.objects.all()})