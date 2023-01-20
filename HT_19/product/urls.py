from django.urls import path
from product.views import products, product_details


app_name = 'products'
urlpatterns = [
    path('', products, name='list'),

    path('<int:pid>/', product_details, name='details'),
]
