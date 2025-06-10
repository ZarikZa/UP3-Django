from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass

@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    pass

@admin.register(CountryProivodstva)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Brand)
class CollectionAdmin(admin.ModelAdmin):
    pass

@admin.register(Products)
class ClothesAdmin(admin.ModelAdmin):
    pass

@admin.register(Clients)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class CollectionAdmin(admin.ModelAdmin):
    pass

@admin.register(Cart)
class ClothesAdmin(admin.ModelAdmin):
    pass

@admin.register(Bill)
class ClothesAdmin(admin.ModelAdmin):
    pass