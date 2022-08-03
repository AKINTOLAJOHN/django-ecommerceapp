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
from DjangoEcommerce.staffapp.models import profile
from DjangoEcommerce.staffapp.forms import SignUpForm, Staff_form, User_form, Customer_form

# Create your views here.
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
def approve(request):
    """
    to loop through the database and send all the item to the viewproduct so admin can see the item which the staff add 
    """
    productItem = Product.objects.all()
    return render(request, 'shopapp/viewproduct.html', {'productItem': productItem })

@login_required
def products(request):
    """
    to loop through the database and send all the item in the shop to the font end
    """
    products = Product.objects.all()
    return render(request, 'shopapp/shop.html', {'products':products})


        
@login_required
def addToCart(request, product_id):
        """
        to loop through the database and send the item at the index of product id 
        """
        viewGood = Product.objects.all().filter(id = product_id)
        if request.method == 'POST':
            form = AddToCart_form(request.POST)
            if form.is_valid():
                quantity = form.cleaned_data["quantity"]
            if viewGood:
                for i in viewGood:
                    price = int(quantity) * float(i.price)
                post = Cart(price_item =price,quantity =quantity)
                post.user_id =request.user.id
                post.product_id = product_id
                post.save()
                print(post)
            
            return HttpResponsePermanentRedirect(reverse('dashboard'))
        else:
            form = AddToCart_form(request.POST)
            return render(request, 'shopapp/viewInDetails.html', {'viewGood': viewGood, 'form':form})

@login_required
def cartItem(request, user_id):
    com = 0
    itemCart = Cart.objects.all().filter(user_id = user_id, purchased = False)
    for item in itemCart:
        com += int(item.price_item)
    return render(request, 'shopapp/cart.html', {'products': itemCart, 'com' : com})

# def checkout(request):
#     products = Product.objects.all()
#     return render(request, 'shopapp/checkout', {'products':products})

@login_required
def delete_Order(request, product_id):
    Cart.objects.all().filter(id = product_id).delete()
    return  products(request)


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