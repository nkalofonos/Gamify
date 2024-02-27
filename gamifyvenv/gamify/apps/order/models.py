from django.db import models
from django.contrib.auth.models import User
from apps.store.models import Product

class Order(models.Model):
    username = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    paid_amount = models.FloatField(blank=True, null=True)
    payment_intent = models.CharField(max_length=250, blank=True, null=True)
    payment_id = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.username
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.DO_NOTHING)
    price = models.FloatField()

    def __str__(self):
        return str(self.id)


class LibraryItem(models.Model):
    username = models.CharField(max_length=100, null=True)
    game = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    installed = models.BooleanField(default=False)

    def __str__(self):
        return self.username