from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from basket.forms import BasketAddProductForm
from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404

def first_view(request):
    return render(request, 'first.html')

def second_view(request):
    return render(request, 'second.html')

def contacts_view(request):
    return render(request, 'contacts.html')

def location_view(request):
    return render(request, 'location.html')



class CategoryListViewMain(ListView):
    model = Category
    template_name = 'categories.html'
    context_object_name = 'categories'

def cart_view(request):
    return render(request, 'basket/basket_detail.html')

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
class ProductListView_Main(ListView):
    model = Products
    template_name = 'products.html'
    context_object_name = 'productss'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_basket'] = BasketAddProductForm()
        return context


class ProductListView(ListView):
    model = Products
    template_name = 'productss/productss_list.html'
    context_object_name = 'productss'


class ProductListViewSort(ListView):
    model = Products
    template_name = 'products.html'
    context_object_name = 'productss'

    def get_queryset(self):
        category_id = self.kwargs.get('category')
        return Products.objects.filter(category__id=category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, pk=self.kwargs.get('category'))
        context['category'] = category
        context['form_basket'] = BasketAddProductForm()
        return context


class ProductDetailView(DetailView):
    model = Products
    template_name = 'productss/productss_detail.html'
    context_object_name = 'productss'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_basket'] = BasketAddProductForm()
        return context

class ProductDetailViewMain(DetailView):
    model = Products
    template_name = 'product_detail_main.html'
    context_object_name = 'productss'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_basket'] = BasketAddProductForm()
        return context

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

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('products_view')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})

def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            login(request, form.save())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('products_view')
    else:
        form = RegistrationForm()
    return render(request, 'auth/registration.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('products_view')