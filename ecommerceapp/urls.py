"""ecommerceapp URL Configuration

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
from django.views.generic import TemplateView 
from re import template
from unicodedata import name
from ecommerceapp.staffapp.views import SignUpView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
     re_path(r'', TemplateView.as_view(template_name='homepage/index.html'), name='index'),
    re_path(r'about', TemplateView.as_view(template_name='homepage/about.html'), name='about'),
    re_path(r'contact', TemplateView.as_view(template_name='homepage/contact.html'), name='contact'),
    re_path(r'Home', TemplateView.as_view(template_name='homepage/index.html'), name='home'),
    #AUTH
    re_path(r'^accounts/', include('django.contrib.auth.urls')), 
    re_path(r'^accounts/signup/$', SignUpView.as_view(), name='signup'),
    re_path(r'^accounts/', include('ecommerceapp.staffapp.urls')),
    # DASHBOARD
    re_path(r'', include(('ecommerceapp.shopapp.urls'))),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
