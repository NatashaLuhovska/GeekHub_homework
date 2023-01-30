from django.urls import path

from product.views import products, product_details, products_from_category, update_product, save_changes,\
    remove_product


app_name = 'products'
urlpatterns = [
    path('', products, name='list'),

    path('<int:pid>/', product_details, name='details'),

    path('category/<int:cid>', products_from_category, name='from-category'),

    path('update/<int:pid>', update_product, name='product-update'),

    path('update/save-changes', save_changes, name='save-changes'),

    path('update/remove', remove_product, name='remove-product'),


]
