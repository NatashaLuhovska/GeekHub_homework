from django.shortcuts import render, get_object_or_404
from product.forms import AddProductToCartForm
from .models import Product


def products(request):
    all_products = Product.objects.all()
    return render(request, 'product/product_list.html', context={'all_products': all_products})


def product_details(request, pid):
    product = get_object_or_404(Product, id=pid)
    form_add_to_cart = AddProductToCartForm(initial={'product_id': product.id, 'quantity': 1})
    return render(request, 'product/product_details.html', context={'product': product, 'form': form_add_to_cart})

