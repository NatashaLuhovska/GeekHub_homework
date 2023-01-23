from django.urls import path
from cart.views import view_cart, add_to_cart, change_quantity, remove_product_of_cart, clear_cart


app_name = 'cart'

urlpatterns = [
    path('', view_cart, name='view'),
    path('addtocart', add_to_cart, name='add'),
    path('changequantity', change_quantity, name='change-quantity'),
    path('remove-product-of-cart', remove_product_of_cart, name='remove-product-of-cart'),
    path('clear-cart', clear_cart, name='clear-cart'),
]
