from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime


# Create your models here.




class Product(models.Model):

    categories = [
        ('Men', 'Men'),
        ('Women', 'Women'),
    ]

    categories = models.CharField(choices=categories, unique=False, max_length=20, null=True)
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    product_image = models.ImageField(upload_to='product_image/', unique=False, null=True)
    item_validation = models.BooleanField(default=False, unique=False)




class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price_item = models.FloatField(blank=True)
    purchased =models.BooleanField(default=False, unique =False)
    delivered =models.BooleanField(default=False, unique =False)
    delivery_agent =models.IntegerField(unique=False, null=True)
