from django import forms
from .models import *

class ClothesForm(forms.ModelForm):
    class Meta:
        model = Clothes
        #Все поля которые нужно заполнять
        fields = ['name', 'disctiption', 'price', 'size', 'color', 'photo', 'is_exists', 'category', 'collection']

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        #Все поля которые нужно заполнять
        fields = ['name', 'disctiption', 'price', 'photo', 'category', 'country', 'brand']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        # Все поля которые нужно заполнять
        fields = ['name', 'disctiption', 'photo']

class CountryProivodstvaForm(forms.ModelForm):
    class Meta:
        model = CountryProivodstva
        # Все поля которые нужно заполнять
        fields = ['country']

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']

class ClentsForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['clientName', 'clientSurname', 'clientMiddleName', 'login', 'password']

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['client', 'product']