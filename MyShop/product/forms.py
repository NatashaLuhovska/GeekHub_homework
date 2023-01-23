from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class AddProductToCartForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])


class ProductIdForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())


