from django.shortcuts import render
from .models import MenuItem

def home(request):
    main_menu = MenuItem.objects.filter(menu_name='main_menu', is_active=True, parent=None)
    all_menu_items = MenuItem.objects.filter(is_active=True)
    return render(request, 'MenuLinks/home.html', {'main_menu': main_menu, 'all_menu_items': all_menu_items})

def about(request):
    main_menu = MenuItem.objects.filter(menu_name='main_menu', is_active=True, parent=None)
    all_menu_items = MenuItem.objects.filter(is_active=True)
    return render(request, 'MenuLinks/about.html', {'main_menu': main_menu, 'all_menu_items': all_menu_items})


def services(request):
    main_menu = MenuItem.objects.filter(menu_name='main_menu', is_active=True, parent=None)
    all_menu_items = MenuItem.objects.filter(is_active=True)
    return render(request, 'MenuLinks/services.html', {'main_menu': main_menu, 'all_menu_items': all_menu_items})


def programming(request):
    main_menu = MenuItem.objects.filter(menu_name='main_menu', is_active=True, parent=None)
    all_menu_items = MenuItem.objects.filter(is_active=True)
    return render(request, 'MenuLinks/programming.html', {'main_menu': main_menu, 'all_menu_items': all_menu_items})


def web_development(request):
    main_menu = MenuItem.objects.filter(menu_name='main_menu', is_active=True, parent=None)
    all_menu_items = MenuItem.objects.filter(is_active=True)
    return render(request, 'MenuLinks/web_development.html', {'main_menu': main_menu, 'all_menu_items': all_menu_items})


def design(request):
    main_menu = MenuItem.objects.filter(menu_name='main_menu', is_active=True, parent=None)
    all_menu_items = MenuItem.objects.filter(is_active=True)
    return render(request, 'MenuLinks/design.html', {'main_menu': main_menu, 'all_menu_items': all_menu_items})


def advertising(request):
    main_menu = MenuItem.objects.filter(menu_name='main_menu', is_active=True, parent=None)
    all_menu_items = MenuItem.objects.filter(is_active=True)
    return render(request, 'MenuLinks/advertising.html', {'main_menu': main_menu, 'all_menu_items': all_menu_items})


def products(request):
    main_menu = MenuItem.objects.filter(menu_name='main_menu', is_active=True, parent=None)
    all_menu_items = MenuItem.objects.filter(is_active=True)
    return render(request, 'MenuLinks/products.html', {'main_menu': main_menu, 'all_menu_items': all_menu_items})


def product_a(request):
    main_menu = MenuItem.objects.filter(menu_name='main_menu', is_active=True, parent=None)
    all_menu_items = MenuItem.objects.filter(is_active=True)
    return render(request, 'MenuLinks/product_a.html', {'main_menu': main_menu, 'all_menu_items': all_menu_items})


def product_b(request):
    main_menu = MenuItem.objects.filter(menu_name='main_menu', is_active=True, parent=None)
    all_menu_items = MenuItem.objects.filter(is_active=True)
    return render(request, 'MenuLinks/product_b.html', {'main_menu': main_menu, 'all_menu_items': all_menu_items})


def contact(request):
    main_menu = MenuItem.objects.filter(menu_name='main_menu', is_active=True, parent=None)
    all_menu_items = MenuItem.objects.filter(is_active=True)
    return render(request, 'MenuLinks/contact.html', {'main_menu': main_menu, 'all_menu_items': all_menu_items})
