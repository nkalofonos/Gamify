from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from apps.cart.cart import Cart

from .models import Product

def api_add_to_cart(request):
    jsonresponse = {'success': True}
    product_id = request.POST.get('product_id')
    update = request.POST.get('update')
    quantity = request.POST.get('quantity',1)

    cart = Cart(request)

    product = get_object_or_404(Product, pk=product_id)

    if not update:
        cart.add(product=product,quantity=1,update_quantity=False)
    else:
        cart.add(product=product,quantity=quantity,update_quantity=True)
    
    return JsonResponse(jsonresponse)