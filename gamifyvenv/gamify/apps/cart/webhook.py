import json
import stripe

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .cart import Cart

from apps.order.models import Order


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
        
        order = Order.objects.get(payment_id=session.id)
        order.payment_intent = session.payment_intent
        order.save()
        order.paid = True
        order.save()
        print('paymentintent wb: ',order.payment_intent)
        
    return HttpResponse(status=200)
    