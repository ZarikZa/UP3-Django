from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import *

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

class ClothesListView(ListView):
    model = Clothes
    template_name = 'clothes/clothes_list.html'
    context_object_name = 'clothes'

class ClothesDetailView(DetailView):
    model = Clothes
    template_name = 'clothes/clothes_detail.html'
    context_object_name = 'clothes'

class ClothesCreateView(CreateView):
    model = Clothes
    form_class = ClothesForm
    template_name = 'clothes/clothes_form.html'
    success_url = reverse_lazy('clothes_list_view')

class ClothesUpdateView(UpdateView):
    model = Clothes
    form_class = ClothesForm
    template_name = 'clothes/clothes_form.html'
    success_url = reverse_lazy('clothes_list_view')

class ClothesDeleteView(DeleteView):
    model = Clothes
    context_object_name = 'clothes'
    template_name = 'clothes/clothes_confirm.html'
    success_url = reverse_lazy('clothes_list_view')
