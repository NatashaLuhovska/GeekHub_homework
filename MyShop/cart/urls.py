from django.urls import path
from cart.views import view_cart, add_to_cart, remove_product_of_cart, clear_cart, cart_total_quantity


app_name = 'cart'

urlpatterns = [
    path('', view_cart, name='view'),

    path('addtocart/<str:addchange>', add_to_cart, name='add'),

    path('remove-product-of-cart', remove_product_of_cart, name='remove-product-of-cart'),

    path('clear-cart', clear_cart, name='clear-cart'),

    path('api/total-quantity', cart_total_quantity, name='api-total-quantity'),

]
