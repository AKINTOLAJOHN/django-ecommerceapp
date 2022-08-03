"""DjangoEcommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from re import template
from unicodedata import name
from django.views.generic import TemplateView 
from DjangoEcommerce.staffapp.views import SignUpView
from DjangoEcommerce.shopapp.views import productView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # landing
    path('',TemplateView.as_view(template_name='index.html'), name='index'),
    re_path(r'^Home',TemplateView.as_view(template_name='index.html'), name="home"),
    re_path(r'^Blog',TemplateView.as_view(template_name='blog.html'), name="blog"),
    re_path(r'^Contact',TemplateView.as_view(template_name='contact.html'), name="contact"),
    re_path(r'^About',TemplateView.as_view(template_name='about.html'), name="about"),
    # DASHBOARD
    re_path(r'', include(('DjangoEcommerce.shopapp.urls'))),
    re_path(r'^dashboard/about/$',TemplateView.as_view(template_name='main_about.html'), name="mainabout"),
    re_path(r'^dashboard/blog/$',TemplateView.as_view(template_name='main_blog.html'), name="mainblog"),
    re_path(r'^dashboard/contact/$',TemplateView.as_view(template_name='main_contact.html'), name="maincontact"),
    # AUTH
    re_path(r'^accounts/', include('django.contrib.auth.urls')), 
    re_path(r'^accounts/signup/$', SignUpView.as_view(), name='signup'),
    re_path(r'^accounts/', include('DjangoEcommerce.staffapp.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
