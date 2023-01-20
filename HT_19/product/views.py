from django.shortcuts import render, get_object_or_404

from .models import Product


def products(request):
    all_products = Product.objects.all()
    return render(request, 'product/product_list.html', context={'all_products': all_products})

def product_details(request, pid):
    product = get_object_or_404(Product, id=pid)
    return render(request, 'product/product_details.html', context={'product': product})
