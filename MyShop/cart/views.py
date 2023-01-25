from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_http_methods

from product.forms import AddProductToCartForm, ProductIdForm
from product.models import Product


def view_cart(request):
    print(request.session.items())
    request.session.setdefault('cart', {})
    cart = request.session.get('cart')
    products = list(Product.objects.filter(id__in=cart.keys()))
    total_price_in_cart = 0
    for product in products:
        product.in_cart_quantity = cart[str(product.id)]
        product.form_q = AddProductToCartForm(initial={'product_id': product.id, 'quantity': 1})
        product.form_id = ProductIdForm(initial={'product_id': product.id})
        total_price_in_cart += product.current_price * product.in_cart_quantity

    context = {
        'products': products,
        'total_price': total_price_in_cart,
    }
    return render(request, 'cart/index.html', context=context)


@require_http_methods(['POST'])
def add_to_cart(request):
    form = AddProductToCartForm(request.POST)
    if not form.is_valid():
        return redirect(reverse('products:list'))

    data = form.cleaned_data
    cart = request.session.setdefault('cart', {})
    product = Product.objects.get(id=data['product_id'])
    if product.current_price > 0:
        cart.setdefault(str(data['product_id']), 0)
        cart[str(data['product_id'])] += data['quantity']
        request.session.modified = True
    return redirect(reverse('products:details', kwargs={'pid': data['product_id']}))


@require_http_methods(['POST'])
def change_quantity(request):
    form = AddProductToCartForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        cart = request.session.get('cart')
        cart[str(data['product_id'])] = data['quantity']
        request.session.modified = True
    return redirect(reverse('cart:view'))


@require_http_methods(['POST'])
def remove_product_of_cart(request):
    form = ProductIdForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        cart = request.session.get('cart')
        cart.pop(str(data['product_id']))
        request.session.modified = True
    return redirect(reverse('cart:view'))


@require_http_methods(['POST'])
def clear_cart(request):
    cart = request.session.get('cart')
    cart.clear()
    request.session.modified = True
    return redirect(reverse('cart:view'))
