from django.shortcuts import render


def home_page(request):
    return render(request, 'third_task/home.html')


def shop_page(request):
    context = {
        'name1': 'Игра 1',
        'name2': 'Игра 2',
        'name3': 'Игра 3',
    }
    return render(request, 'third_task/shop.html', context)


def cart_page(request):
    return render(request, 'third_task/cart.html')
