from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from apps.order.models import LibraryItem
from apps.store.models import Product

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

@login_required
def myaccount(request):
    return render(request, 'myaccount.html')

def library(request, game_title=None):
    if request.user.is_authenticated:
        game_title = request.session.get('game_title')
        print(game_title)
        if 'game_title' in request.session:
            del request.session['game_title']
        flag = 0
        if (game_title) is not None:
            flag = 1
            game_load = Product.objects.filter(title=game_title)
            for game in game_load:
                title = game.title
                category = game.category
                image = game.image
                description = game.description

        library_items = LibraryItem.objects.filter(username=request.user).order_by('game__title')


        installed = False

        lib_item = LibraryItem.objects.filter(username=request.user, game__title=game_title)
        for item in lib_item:
            installed = item.installed


        if(flag ==1):
            context = { 
                'library_items': library_items,
                'category': category,
                'image': image,
                'description': description,
                'title': title,
                'flag': flag,
                'installed': installed
            }
        else:
            context = { 
                'library_items': library_items,
                'flag': flag,
                'installed': installed
            }
        return render(request, 'library.html', context)
    
    return render(request, 'library.html')


