import datetime
import os

from random import randint

from apps.cart.cart import Cart


from apps.order.models import Order, OrderItem


def checkout(request, username):
    order = Order(username=username)
    order.save()

    cart = Cart(request)

    for item in cart:
        OrderItem.objects.create(order=order,product=item['product'], price=item['price'])
    
    return order.id
