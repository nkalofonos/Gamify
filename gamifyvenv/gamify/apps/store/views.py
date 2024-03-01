from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q


from .models import Product, Category, ProductReview
from apps.order.models import LibraryItem
from apps.cart.cart import Cart
from apps.userprofile.views import library


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

    #Add review
    if request.method =='POST' and request.user.is_authenticated:
        stars = request.POST.get('stars', 3)
        content = request.POST.get('content', '')

        review = ProductReview.objects.create(product=product, user=request.user, stars=stars, content=content)

        return redirect('product_detail', category_slug=category_slug, slug=slug)

    #Flag if user has game in library
    has_game = 0
    #Flag if user has game in cart
    in_cart = 0
    cart = Cart(request)

    #Checks if game is in cart
    for item in cart:
        product1 = item['product']
        if (product == product1):
            in_cart = 1

    #Checks if game is in library
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