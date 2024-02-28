from django.conf import settings
from django.shortcuts import render, redirect

from .cart import Cart
from apps.order.models import LibraryItem

def cart_detail(request):
    cart = Cart(request)
    productsstring = ''
    owned_games = []
    flag = 0
    if request.user.is_authenticated:
        library_items = LibraryItem.objects.filter(username=request.user)
        for game in library_items:
            title = game.game.title
            owned_games.append(title)
        print('owned_games :', owned_games)
    

    for item in cart:
        product = item['product']
        url = '/%s/%s/' % (product.category.slug, product.slug)
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s', 'thumbnail': '%s', 'url': '%s'}," % (product.id, product.title, product.price, item['quantity'], item['total_price'], product.thumbnail.url, url)
        if product.title in owned_games:
            flag = 1
        productsstring = productsstring + b
        print('product:', product)
        print(flag)
    context = {
        'cart': cart,
        'pub_key': settings.STRIPE_API_KEY_PUBLISHABLE,
        'productsstring': productsstring,
        'flag': flag
    }

    return render(request, 'cart.html', context)

def success(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'success.html')