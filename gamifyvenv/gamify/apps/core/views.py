from django.shortcuts import render
from apps.store.models import Product

# Create your views here.

def frontpage(request):
    fproducts = Product.objects.filter(is_featured=True)
    products = Product.objects.all

    context = {
        'fproducts': fproducts,
        'products': products
    }
    return render(request, 'frontpage.html', context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')