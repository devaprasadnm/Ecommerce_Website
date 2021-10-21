from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    special=models.BooleanField(default=False)


class Products(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    category =models.ForeignKey(Category,on_delete=models.CASCADE,default=False)

class Cart(models.Model):
    pid = models.ForeignKey(Products, on_delete=models.CASCADE)
    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)

class Order(models.Model):
    cartid = models.ForeignKey(Cart,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    Phone = models.CharField(max_length=13)