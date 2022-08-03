from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from DjangoEcommerce.shopapp import views as shopapp_view

urlpatterns =[
    re_path(r'shop/', shopapp_view.products, name='dashboard'),
    re_path(r'add_product', shopapp_view.productView, name='add'),
    re_path(r'view_product', shopapp_view.approve, name='viewgoods'),
    re_path(r'^itemVerify/(?P<product_id>\d+)/', shopapp_view.deapproval, name="deapproval"),
    re_path(r'product_description/(?P<product_id>\d+)/', shopapp_view.addToCart, name='viewItem'),
    re_path(r'cartproduct/(?P<user_id>\d+)/', shopapp_view.cartItem, name='cart'),
    re_path(r'removeFromCart/(?P<product_id>\d+)', shopapp_view.delete_Order, name='delete_Order'),
]