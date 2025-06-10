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

#
#Brand
#

class BrandListView(ListView):
    model = Brand
    template_name = 'brand/brand_list.html'
    context_object_name = 'brands'

class BrandDetailView(DetailView):
    model = Brand
    template_name = 'brand/brand_detail.html'
    context_object_name = 'brands'

class BrandCreateView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'brand/brand_form.html'
    success_url = reverse_lazy('brands_list_view')

class BrandUpdateView(UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'brand/brand_form.html'
    success_url = reverse_lazy('brands_list_view')

class BrandDeleteView(DeleteView):
    model = Brand
    context_object_name = 'brands'
    template_name = 'brand/brand_confirm_delete.html'
    success_url = reverse_lazy('brands_list_view')

#
#Category
#

class CategoryListView(ListView):
    model = Category
    template_name = 'categories/categories_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/categories_detail.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/categories_form.html'
    success_url = reverse_lazy('categories_list_view')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/categories_form.html'
    success_url = reverse_lazy('categories_list_view')

class CategoryDeleteView(DeleteView):
    model = Category
    context_object_name = 'categories'
    template_name = 'categories/categories_confirm_delete.html'
    success_url = reverse_lazy('categories_list_view')
#
#Country
#

class CountryListView(ListView):
    model = CountryProivodstva
    template_name = 'countries/countries_list.html'
    context_object_name = 'countries'

class CountryDetailView(DetailView):
    model = CountryProivodstva
    template_name = 'countries/countries_detail.html'
    context_object_name = 'countries'

class CountryCreateView(CreateView):
    model = CountryProivodstva
    form_class = CountryProivodstvaForm
    template_name = 'countries/countries_form.html'
    success_url = reverse_lazy('countries_list_view')

class CountryUpdateView(UpdateView):
    model = CountryProivodstva
    form_class = CountryProivodstvaForm
    template_name = 'countries/countries_form.html'
    success_url = reverse_lazy('countries_list_view')

class CountryDeleteView(DeleteView):
    model = CountryProivodstva
    context_object_name = 'countries'
    template_name = 'countries/countries_confirm_delete.html'
    success_url = reverse_lazy('countries_list_view')

#
#Product
#

class ProductListView(ListView):
    model = Products
    template_name = 'productss/productss_list.html'
    context_object_name = 'productss'

class ProductDetailView(DetailView):
    model = Products
    template_name = 'productss/productss_detail.html'
    context_object_name = 'productss'

class ProductCreateView(CreateView):
    model = Products
    form_class = ProductsForm
    template_name = 'productss/productss_form.html'
    success_url = reverse_lazy('productss_list_view')

class ProductUpdateView(UpdateView):
    model = Products
    form_class = ProductsForm
    template_name = 'productss/productss_form.html'
    success_url = reverse_lazy('productss_list_view')

class ProductDeleteView(DeleteView):
    model = Products
    context_object_name = 'productss'
    template_name = 'productss/productss_confirm_delete.html'
    success_url = reverse_lazy('productss_list_view')
#
#Wishlist
#

class WishlistListView(ListView):
    model = Wishlist
    template_name = 'wishlist/wishlist_list.html'
    context_object_name = 'wishlist'

class WishlistDetailView(DetailView):
    model = Wishlist
    template_name = 'wishlist/wishlist_detail.html'
    context_object_name = 'wishlist'

class WishlistCreateView(CreateView):
    model = Wishlist
    form_class = WishlistForm
    template_name = 'wishlist/wishlist_form.html'
    success_url = reverse_lazy('wishlist_list_view')

class WishlistUpdateView(UpdateView):
    model = Wishlist
    form_class = WishlistForm
    template_name = 'wishlist/wishlist_form.html'
    success_url = reverse_lazy('wishlist_list_view')

class WishlistDeleteView(DeleteView):
    model = Wishlist
    context_object_name = 'wishlist'
    template_name = 'wishlist/wishlist_confirm_delete.html'
    success_url = reverse_lazy('wishlist_list_view')
