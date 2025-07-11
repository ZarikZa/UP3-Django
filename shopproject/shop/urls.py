
from django.contrib import admin
from django.urls import path, include
from .views import *
from basket.views import *
urlpatterns = [
    path('', first_view, name='first_view'),
    path('first/', first_view, name='first_view'),
    path('second/', second_view, name='second_view'),
    path('contacts/', contacts_view, name='contacts_view'),
    path('location/', location_view, name='location_view'),
    path('products/', ProductListView_Main.as_view(), name='products_view'),
    path('category/', CategoryListViewMain.as_view(), name='categories_view'),
    path('category/<str:category>', ProductListViewSort.as_view(), name='categories_sort_view'),
    path('basket/', basket_detail, name='basket_detail'),
    path('products/<int:pk>', ProductDetailViewMain.as_view(), name='product_detail_view'),

    path('login/', login_user, name='login_user'),
    path('registration/', registration_user, name='registration_user'),
    path('logout/', logout_user, name='logout_user'),

    path('clothes/', ClothesListView.as_view(), name='clothes_list_view'),
    path('clothes/<int:pk>/', ClothesDetailView.as_view(), name='clothes_detail_view'),
    path('clothes/create/', ClothesCreateView.as_view(), name='clothes_create_view'),
    path('clothes/<int:pk>/update/', ClothesUpdateView.as_view(), name='clothes_update_view'),
    path('clothes/<int:pk>/delete/', ClothesDeleteView.as_view(), name='clothes_delete_view'),


    path('brands/', BrandListView.as_view(), name='brands_list_view'),
    path('brands/<int:pk>/', BrandDetailView.as_view(), name='brands_detail_view'),
    path('brands/create/', BrandCreateView.as_view(), name='brands_create_view'),
    path('brands/<int:pk>/update/', BrandUpdateView.as_view(), name='brands_update_view'),
    path('brands/<int:pk>/delete/', BrandDeleteView.as_view(), name='brands_delete_view'),

    path('categories/', CategoryListView.as_view(), name='categories_list_view'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='categories_detail_view'),
    path('categories/create/', CategoryCreateView.as_view(), name='categories_create_view'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='categories_update_view'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='categories_delete_view'),

    path('countries/', CountryListView.as_view(), name='countries_list_view'),
    path('countries/<int:pk>/', CountryDetailView.as_view(), name='countries_detail_view'),
    path('countries/create/', CountryCreateView.as_view(), name='countries_create_view'),
    path('countries/<int:pk>/update/', CountryUpdateView.as_view(), name='countries_update_view'),
    path('countries/<int:pk>/delete/', CountryDeleteView.as_view(), name='countries_delete_view'),

    path('productss/', ProductListView.as_view(), name='productss_list_view'),
    path('productss/<int:pk>/', ProductDetailView.as_view(), name='productss_detail_view'),
    path('productss/create/', ProductCreateView.as_view(), name='productss_create_view'),
    path('productss/<int:pk>/update/', ProductUpdateView.as_view(), name='productss_update_view'),
    path('productss/<int:pk>/delete/', ProductDeleteView.as_view(), name='productss_delete_view'),

    path('wishlist/', WishlistListView.as_view(), name='wishlist_list_view'),
    path('wishlist/<int:pk>/', WishlistDetailView.as_view(), name='wishlist_detail_view'),
    path('wishlist/create/', WishlistCreateView.as_view(), name='wishlist_create_view'),
    path('wishlist/<int:pk>/update/', WishlistUpdateView.as_view(), name='wishlist_update_view'),
    path('wishlist/<int:pk>/delete/', WishlistDeleteView.as_view(), name='wishlist_delete_view'),

]