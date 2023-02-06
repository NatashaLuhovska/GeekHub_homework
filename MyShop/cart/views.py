from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.http.response import JsonResponse

from product.forms import AddProductToCartForm, ProductIdForm
from product.models import Product


def view_cart(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Only for authenticated users! Please login!')
        return redirect(reverse('login'))
    request.session.setdefault('cart', {})
    cart = request.session.get('cart')
    products = list(Product.objects.filter(id__in=cart.keys()))
    total_price_in_cart = 0
    for product in products:
        product.in_cart_quantity = cart[str(product.id)]
        product.form_q = AddProductToCartForm(initial={'product_id': product.id, 'quantity': product.in_cart_quantity})
        product.form_id = ProductIdForm(initial={'product_id': product.id})
        total_price_in_cart += product.current_price * product.in_cart_quantity

    context = {
        'products': products,
        'total_price': total_price_in_cart,
    }
    return render(request, 'cart/index.html', context=context)


@require_http_methods(['POST'])
def add_to_cart(request, addchange):
    if not request.user.is_authenticated:
        messages.error(request, 'Only for authenticated users! Please login!')
        return redirect(reverse('login'))
    form = AddProductToCartForm(request.POST)
    if not form.is_valid():
        return JsonResponse({'message': 'Form is not valid, check the quantity.'}, status=400)

    data = form.cleaned_data
    cart = request.session.setdefault('cart', {})
    product = Product.objects.get(id=data['product_id'])
    if product.current_price > 0:
        cart.setdefault(str(data['product_id']), 0)
        if addchange == 'add':
            cart[str(data['product_id'])] += data['quantity']
            request.session.modified = True
        elif addchange == 'change':
            cart[str(data['product_id'])] = data['quantity']
            request.session.modified = True
        return JsonResponse({'message': 'Product was added to the cart.', 'cart_total_quantity': sum(cart.values())})


@require_http_methods(['POST'])
def remove_product_of_cart(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Only for authenticated users! Please login!')
        return redirect(reverse('login'))
    form = ProductIdForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        cart = request.session.get('cart', {})
        cart.pop(str(data['product_id']))
        request.session.modified = True
    return JsonResponse({'message': 'Product was delete from cart.', 'cart_total_quantity': sum(cart.values())})


@require_http_methods(['POST'])
def clear_cart(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Only for authenticated users! Please login!')
        return redirect(reverse('login'))
    cart = request.session.get('cart')
    cart.clear()
    request.session.modified = True
    return JsonResponse({'cart_total_quantity': 0})


def cart_total_quantity(request):
    cart = request.session.get('cart', {})
    return JsonResponse({'cart_total_quantity': sum(cart.values())})