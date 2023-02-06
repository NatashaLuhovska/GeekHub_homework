from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from rest_framework import authentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission
from rest_framework.pagination import PageNumberPagination

from product.forms import AddProductToCartForm, ProductUpdateForm, ProductIdForm
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


def products(request):
    user = User.objects.first()
    all_products = Product.objects.all()
    all_categories = Category.objects.all()
    return render(request, 'product/product_list.html', context={
        'all_products': all_products,
        'all_categories': all_categories
    })


def product_details(request, pid):
    product = get_object_or_404(Product, id=pid)
    form_add_to_cart = AddProductToCartForm(initial={'product_id': product.id, 'quantity': 1})
    remove_form = ProductIdForm(initial={'product_id': product.id})
    return render(request, 'product/product_details.html', context={
        'product': product,
        'form': form_add_to_cart,
        'remove_form': remove_form
    })


def products_from_category(request, cid):
    category = get_object_or_404(Category, id=cid)
    products_from_cat = list(Product.objects.filter(category=category))
    return render(request, 'product/products_from_category.html', context={
        'products_from_category': products_from_cat
    })


def update_product(request, pid):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to access this page. Only for the site administrator.')
        return redirect(reverse('products:list'))

    product = get_object_or_404(Product, id=pid)
    form = ProductUpdateForm(initial={
        'id': product.id,
        'product_id': product.product_id,
        'title': product.title,
        'old_price': product.old_price,
        'current_price': product.current_price,
        'href': product.href_product,
        'brand': product.brand,
        'category': product.category,
        'description': product.description,
    })
    return render(request, 'product/update_product.html', context={'product': product, 'form': form, })


@require_http_methods(['POST'])
def save_changes(request):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to access this page. Only for the site administrator.')
        return redirect(reverse('products:list'))
    form = ProductUpdateForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        defaults = {
            'product_id': data['product_id'],
            'title': data['title'],
            'old_price': data['old_price'],
            'current_price': data['current_price'],
            'href': data['href'],
            'brand': data['brand'],
            'category': Category.objects.filter(id=data['category'])[0],
            'description': data['description'],
        }
        Product.objects.update_or_create(id=data['id'], defaults=defaults)
    return redirect(reverse('products:list'))


@require_http_methods(['POST'])
def remove_product(request):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to access this page. Only for the site administrator.')
        return redirect(reverse('products:list'))
    form = ProductIdForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        Product.objects.filter(id=data['product_id']).delete()
    return redirect(reverse('products:list'))


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['retrieve', 'list']:
            return request.user.is_authenticated
        elif view.action == ['create', 'update', 'partial_update', 'destroy']:
            return request.user.is_superuser
        else:
            return False


class MyPagination(PageNumberPagination):
    page_size = 5


class ProductApiView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (UserPermission,)
    pagination_class = MyPagination


class CategoryApiView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (UserPermission,)
    pagination_class = MyPagination
