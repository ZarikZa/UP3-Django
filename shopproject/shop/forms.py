from django import forms
from .models import *

class ClothesForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = ['name', 'disctiption', 'price', 'size', 'color', 'photo', 'is_exists', 'category', 'collection']


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'disctiption', 'price', 'photo', 'category', 'country', 'brand']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'disctiption': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'country': forms.Select(attrs={'class': 'form-select'}),
            'brand': forms.Select(attrs={'class': 'form-select'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'disctiption', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'disctiption': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class CountryProivodstvaForm(forms.ModelForm):
    class Meta:
        model = CountryProivodstva
        fields = ['country']
        widgets = {
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ClentsForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['clientName', 'clientSurname', 'clientMiddleName', 'login', 'password']
        widgets = {
            'clientName': forms.TextInput(attrs={'class': 'form-control'}),
            'clientSurname': forms.TextInput(attrs={'class': 'form-control'}),
            'clientMiddleName': forms.TextInput(attrs={'class': 'form-control'}),
            'login': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['client', 'product']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-select'}),
            'product': forms.Select(attrs={'class': 'form-select'}),
        }
