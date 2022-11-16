from django.contrib import admin

# Register your models here.

from .models import Product, Contact, Order, Order_track
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(Order_track)
