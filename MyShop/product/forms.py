from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Category


class AddProductToCartForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])


class ProductIdForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())


class ProductUpdateForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    product_id = forms.CharField(max_length=20)
    title = forms.CharField(max_length=200)
    old_price = forms.DecimalField(max_digits=10, decimal_places=2)
    current_price = forms.DecimalField(max_digits=10, decimal_places=2)
    href = forms.CharField(max_length=256)
    brand = forms.CharField(max_length=120)
    category_list = []
    for category in Category.objects.all():
        category_list.append((category.id, category.category_title))
    category = forms.ChoiceField(choices=category_list)
    description = forms.CharField(required=False, widget=forms.Textarea)



