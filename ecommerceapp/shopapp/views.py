from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Product, Cart
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib import messages
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from .forms import Product_Form, AddToCart_form
from ecommerceapp.staffapp.models import profile
from ecommerceapp.staffapp.forms import SignUpForm, Staff_form, User_form, Customer_form



@login_required
def products(request):
    """
    to loop through the database and send all the item in the shop to the font end
    """
    products = Product.objects.all()
    return render(request, 'shopapp/shop.html', {'products':products})


@login_required
def approve(request):
    """
    to loop through the database and send all the item to the viewproduct so admin can see the item which the staff add 
    """
    productItem = Product.objects.all()
    return render(request, 'shopapp/viewproduct.html', {'productItem': productItem })


@login_required
def productView(request):
    """
    to send the form to add product and insert in the database 
    """
    if request.method == 'POST':
        form = Product_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            form = Product_Form(request.POST, request.FILES)
        return render(request, 'shopapp/shop.html',{
            'form' : form
        })
    else:
        form = Product_Form(request.POST, request.FILES)
        return render(request, 'shopapp/addproduct.html',{
            'form': form
    })

@login_required
def deapproval(request, product_id):
    """
    for the superuser to be able to approval item that can be see by the customer 
    """
    goods = Product.objects.get(id = product_id)
    if goods.item_validation:
        goods.item_validation = 0
    else:
        goods.item_validation = 1
    goods.save()
    return approve(request)