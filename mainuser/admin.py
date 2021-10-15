from django.contrib import admin

# Register your models here.

from .models import Products,Category,Cart

admin.site.register(Products)
admin.site.register(Category) 
admin.site.register(Cart) 