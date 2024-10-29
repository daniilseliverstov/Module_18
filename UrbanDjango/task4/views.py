from django.shortcuts import render


def home_page(request):
    return render(request, 'fourth_task/home.html')


def shop_page(request):
    context = {
        'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay2'],

    }
    return render(request, 'fourth_task/shop.html', context)


def cart_page(request):
    return render(request, 'fourth_task/cart.html')
