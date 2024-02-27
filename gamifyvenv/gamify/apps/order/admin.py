from django.contrib import admin

from .models import Order, OrderItem, LibraryItem


admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(LibraryItem)
# Register your models here.
