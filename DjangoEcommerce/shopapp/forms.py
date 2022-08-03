from django import forms
from .models import Cart, Product

class Product_Form(forms.ModelForm):
   class Meta:
       model = Product
       fields = [
            'product_image',
            'product_name',
            'categories',
            'price',
            'description',
        ]

class AddToCart_form(forms.ModelForm):
    class Meta:
        model = Cart
        fields =[
            'quantity'
        ]


# class PaymentOption_form(forms.Form):
#     class meta:
#         fields =[
#             'option',
#             'card_number'
#         ]