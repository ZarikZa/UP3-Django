from django import forms
from .models import Clothes

class ClothesForm(forms.ModelForm):
    class Meta:
        model = Clothes
        #Все поля которые нужно заполнять
        fields = ['name', 'disctiption', 'price', 'size', 'color', 'photo', 'is_exists', 'category', 'collection']

