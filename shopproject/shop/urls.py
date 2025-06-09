
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('first/', first_view, name='first_view'),
    path('second/', second_view, name='second_view'),
    path('contacts/', contacts_view, name='contacts_view'),
    path('location/', location_view, name='location_view'),
    path('products/', products_view, name='products_view'),
    path('categories/', categories_view, name='categories_view'),
    path('cart/', cart_view, name='cart_view'),
]