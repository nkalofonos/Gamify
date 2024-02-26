from django.db import models
from apps.store.models import Product

# Create your models here.
class Order(models.Model):
    username = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paid_amount = models.FloatField(blank=True, null=True)

    peyment_intent = models.FloatField(blank=True,null = True)

    def __str__(self):
        return  '%s' % self.username
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.DO_NOTHING)
    price = models.FloatField()


    def __str__(self):
        return '%s' % self.id