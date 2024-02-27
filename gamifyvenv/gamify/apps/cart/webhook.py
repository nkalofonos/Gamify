import json
import stripe

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .cart import Cart

from apps.order.models import Order, OrderItem, LibraryItem


@csrf_exempt
def webhook(request):
    payload = request.body
    event = None
    stripe.api_key = settings.STRIPE_API_KEY_HIDDEN
    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        return HttpResponse(status=400)
        
    
    if event.type == 'checkout.session.completed':
        session = event.data.object
        
        order1 = Order.objects.get(payment_id=session.id)
        order1.payment_intent = session.payment_intent
        order1.save()
        order1.paid = True
        order1.save()

        for order_item in OrderItem.objects.filter(order=order1):
            print('order')
            library_item = LibraryItem(
                username=order1.username,
                game=order_item.product
            )
            library_item.save()
        
    return HttpResponse(status=200)
    