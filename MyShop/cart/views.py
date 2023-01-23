from django.shortcuts import render, redirect, reverse
from product.forms import AddProductToCartForm, ProductIdForm
from django.views.decorators.http import require_http_methods
from product.models import Product


def view_cart(request):
    print(request.session.items())
    cart = request.session.get('cart')
    products = list(Product.objects.filter(id__in=cart.keys()))
    for product in products:
        product.in_cart_quantity = cart[str(product.id)]
        product.form_q = AddProductToCartForm(initial={'product_id': product.id, 'quantity': 1})
        product.form_id = ProductIdForm(initial={'product_id': product.id})

    context = {
        'products': products,
    }
    return render(request, 'cart/index.html', context=context)


@require_http_methods(['POST'])
def add_to_cart(request):
    if request.method == 'POST':
        form = AddProductToCartForm(request.POST)
        if not form.is_valid():
            return redirect(reverse('products:list'))

        data = form.cleaned_data
        cart = request.session.setdefault('cart', {})
        cart.setdefault(str(data['product_id']), 0)
        cart[str(data['product_id'])] += data['quantity']
        request.session.modified = True
        return redirect(reverse('products:details', kwargs={'pid': data['product_id']}))
    else:
        return redirect(reverse('products:list'))


@require_http_methods(['POST'])
def change_quantity(request):
    if request.method == 'POST':
        form = AddProductToCartForm(request.POST)
        if not form.is_valid():
            print('not valid')
            return redirect(reverse('cart:view'))

        data = form.cleaned_data
        cart = request.session.get('cart')
        cart[str(data['product_id'])] = data['quantity']
        request.session.modified = True
        return redirect(reverse('cart:view'))
    else:
        return render(request, 'cart/index.html')


@require_http_methods(['POST'])
def remove_product_of_cart(request):
    if request.method == 'POST':
        form = ProductIdForm(request.POST)
        if not form.is_valid():
            return redirect(reverse('cart:view'))

        data = form.cleaned_data
        cart = request.session.get('cart')
        cart.pop(str(data['product_id']))
        request.session.modified = True
        return redirect(reverse('cart:view'))
    else:
        return render(request, 'cart/index.html')


@require_http_methods(['POST'])
def clear_cart(request):
    cart = request.session.get('cart')
    cart.clear()
    request.session.modified = True
    return redirect(reverse('cart:view'))
