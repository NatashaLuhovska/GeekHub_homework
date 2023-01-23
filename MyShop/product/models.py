from django.db import models


class Product(models.Model):
    product_id = models.CharField(max_length=20, default='')
    title = models.CharField(max_length=200, default='Default title')
    old_price = models.DecimalField(max_digits=10, decimal_places=2, default='0.00', blank=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    href_product = models.CharField(max_length=256, default='', blank=True)
    brand = models.CharField(max_length=120, default='')
    category = models.CharField(max_length=40, default='')
    description = models.TextField(default='', blank=True)

