from django.shortcuts import render, get_object_or_404
from django.db.models import Q


from .models import Product, Category
from apps.order.models import LibraryItem
from apps.cart.cart import Cart


def search(request):
    query = request.GET.get('query')
    products = Product.objects.filter(Q(title__icontains=query))

    context = {
        'query': query,
        'products': products
    }

    return render(request, 'search.html', context)

def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)
    has_game = 0
    in_cart = 0
    cart = Cart(request)
    for item in cart:
        product1 = item['product']
        if (product == product1):
            in_cart = 1

    if (LibraryItem.objects.filter(username = request.user, game = product)):
        has_game = 1

    context = {
        'product': product,
        'has_game': has_game,
        'in_cart': in_cart
    }

    return render(request, 'product_detail.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()

    context = {
        'category': category,
        'products': products
    }

    return render(request, 'category_detail.html', context)