from django.shortcuts import render

def first_view(request):
    return render(request, 'first.html')

def second_view(request):
    return render(request, 'second.html')

def contacts_view(request):
    return render(request, 'contacts.html')

def location_view(request):
    return render(request, 'location.html')

def products_view(request):
    return render(request, 'products.html')

def categories_view(request):
    return render(request, 'categories.html')

def cart_view(request):
    return render(request, 'cart.html')