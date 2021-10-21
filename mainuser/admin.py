from django.contrib import admin

# Register your models here.

from .models import Products,Category,Cart,Order

admin.site.register(Products)
admin.site.register(Category) 
admin.site.register(Cart) 
admin.site.register(Order) 